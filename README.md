# How to use SyntaxNet

<hr>

[SyntaxNet](https://github.com/tensorflow/models/tree/master/syntaxnet) is a neural-network Natural Language Processing framework for TensorFlow released by Google. It is one of the most powerful and accurate parsers. 

![Syntaxnet Demo]("syntaxnet.gif")

Given a sentence as input, Syntaxnet tags each word with a part-of-speech (POS) tag that describes the word's syntactic function, and it determines the syntactic relationships between words in the sentence, represented in the dependency parse tree. These syntactic relationships are directly related to the underlying meaning of the sentence in question.

## Building SyntaxNet

There are two ways to actually build and run SyntaxNet:

1. Building from source.
2. Using [Docker](https://www.docker.com/).

### 1. Building from source.

You can build SyntaxNet by following the [nice guide](https://github.com/tensorflow/models/tree/master/syntaxnet#manual-installation) provided in the main SyntaxNet github branch. 

### 2. Using Docker.

Building from source is doable but its computationally expensive and can result in few bugs while building if we mess up with the steps provided. Hence a clean way to build SyntaxNet is by using Docker. Here's what we are going to require :

#### Prerequisites:

* A 64-bit computer with at least 2 GB of RAM
* The latest version of Docker
* Ubuntu (I habe only tested it on Ubuntu as of yet.)

Steps:

1. Pulling the Docker Image

There could be other SyntaxNet images, but for demonstration, we'll be pulling an image created by [brianlow](https://github.com/brianlow/syntaxnet-docker).
	
```docker pull brianlow/syntaxnet-docker```

Depending on the speed of your network connection, you might have to wait for a while because the image is about 1GB.

2. Once the SyntaxNet image is installed, you can now test it.  You need to create a new container using it and run a Bash shell on it.

```docker run --name mcparseface --rm -i -t brianlow/syntaxnet-docker bash```

3. Parsey McParseface, the pretrained model that comes with SyntaxNet is powerful but slightly complicated. Thankfully, we can use the handy shell script `demo.sh` provided with SyntaxNet itself. All you need to do is pass an English sentence to it. 

```
echo "I found a website to post AI tutorials ." \
| syntaxnet/demo.sh
```

It generates the folling dependency parse tree as output:
<code>
Input: I found a website to post AI tutorials .
Parse:
found VBD ROOT
 +-- I PRP nsubj
 +-- website NN dobj
 |   +-- a DT det
 |   +-- post VB infmod
 |       +-- to TO aux
 |       +-- tutorials NNS dobj
 |           +-- AI NNP nn
 +-- . . punct
I established a website to post AI tutorials.
</code>

### Using SyntaxNet

Instead of running the shell script, the code in this repo shows you how to use SyntaxNet. I have built a Python wrapper which calls the shell script and runs SyntaxNet. 

* Usage 

```python main.py 'I found a website to post AI tutorials.'```

Basically what this srcipt does is it parses the input sentence, finds the root verb from the sentence using the dependency tree created by SyntaxNet, and then finds a synonym of the root verb and replaces it using the nltk library. (You'll have to run `pip install nltk` to install nltk). The `Verb` folder contains the code to find out the tense of the root verb so that the synonym that will replace it can be of the same tense in order to keep the meaning of the sentence intact.

### Conclusion

Thus this code is a pretty simple approach to use SyntaxNet for basic papraphrasing. It's just a demo and it doesn't always find the paraphrase and hence returns the same sentence. But our main goal was to run SyntaxNet and leverage its capabilities to find the proper context in a given text and use it to find important pieces of text like the Root word, Dependent Object etc.

To learn more about all the Part of Speech Tags that appear in the SyntaxNet output, please visit [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).

And to understand the dependencies that SyntaxNet tries to find within a sentence, please visit [here](http://universaldependencies.org/en/dep/).

This links would definitely help you to understand the output of SyntaxNet better. Feel free to improvise!

<hr>
