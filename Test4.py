# -*- coding: utf-8 -*-
import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
infilePath = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.1.txt"

textDoc = " "
with open(infilePath) as infile:
 	textDoc= infile.read()
infile.close()
removingReferencesPattern = r'[\[\d\]]'
textDoc = re.sub(removingReferencesPattern,"", textDoc)
textDoc = re.sub("[^\w]", " ",  textDoc)
#print(textDoc)
word_tokens  = word_tokenize(textDoc)
#print(word_tokens)
word_tokens_noStopwords = [""]
stopWords = set(stopwords.words("english"))
for w in word_tokens:
	if w not in stopWords: 
		word_tokens_noStopwords.append(w)
print(len(word_tokens_noStopwords))
print(len(word_tokens))


