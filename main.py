"""
Main script to process the input string using nlp_util via the SyntaxNet parsing and finding root verb synonyms with accurate tenses using the Verb class,
and then print the paraphrased sentence.
"""
import nlp_util

#accept user input
input_str = nlp_util.get_user_input()

#return dependency tree
dep_tree = nlp_util.create_dependency_tree()

print "Dependency tree:"
for d in dep_tree:
	print d


#retrieve root word and dependent object
root = nlp_util.get_root_word(dep_tree)
#print root

dobj = nlp_util.get_dependent_object(dep_tree)
#print dobj

#retrieve synonym for root word
synonym = nlp_util.get_synonym(root)
#print synonym

#display parahrased sentence
print "\nParaphrased sentence :\n"
print nlp_util.get_paraphrase(input_str,root)
