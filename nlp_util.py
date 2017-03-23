"""
Helper class that provides NLP functionalities and calls the SyntaxNet shell script.
"""

import sys, os 
import subprocess
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import verb

input_str = ""

#accept user input
def get_user_input():
	input = sys.argv[1]
	input_str = input
	print("Input String: " + input_str)
	return input_str


#return dependency tree
def create_dependency_tree():
	arg_list = sys.argv
	arg_list.pop(0)
	str1 = ' '.join(arg_list)
	p = subprocess.Popen("echo " + str1 + "| sudo docker run --rm -i brianlow/syntaxnet-docker", stdout=subprocess.PIPE, shell=True)
	out = p.stdout.read()
	deptree = out.splitlines()
	return deptree

#retrieve root word 
def get_root_word(dependency_tree):
	root = dependency_tree[2].split()
	return root

#retrieve dependent object
def get_dependent_object(dependency_tree):
	#print "Getting dependency tree"
	#for d in dependency_tree:
	#	print d
	for string in dependency_tree:
		if string.find("dobj") != -1:
			dobj = string.split()[1]
			return dobj

#retrieve synonym for root word
def get_synonym(root):

	listofsyns = wordnet.synsets(root[0])
	synonym = listofsyns[3].name().split(".")[0]
	
	if root[1] =='VBD':
		synonym = verb.verb_past(synonym)
	elif root[1] =='VBG':
		synonym = verb.verb_present_participle(synonym)
	elif root[1] =='VBN':
		synonym = verb.verb_past_participle(synonym)
	elif root[1] =='VBP':
		synonym = verb.verb_present(synonym, person=3, negate=True)
	elif root[1] =='VBZ':
		synonym = verb.verb_present(synonym, person=3, negate=False)
		
	return synonym

#retrieve paraphrased sentence
def get_paraphrase(input_str,root):
	list_str = input_str.split()
	stop = set(stopwords.words('english'))
	paraphrase = []
	for word in list_str:
		try:
			if word == root[0]:
				if word.lower() not in stop:
					paraphrase.append(get_synonym(root))	
			else:
				paraphrase.append(word) 
		except Exception: 
			pass
	paraphrased_str = " ".join(paraphrase)
	return paraphrased_str
	#return paraphrase
