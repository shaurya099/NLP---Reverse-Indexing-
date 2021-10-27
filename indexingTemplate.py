#List of Python functions 
'''
list of imports and headers 
# -*- coding: utf-8 -*-
import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
'''
import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import OrderedDict

#reading a file and storing it in an array 
def readFile(infilePath):
	textDoc = " "
	with open(infilePath) as infile:
 		textDoc= infile.read()
	infile.close()
	return textDoc 

'''
Removing all references -> example word[27] becomes word. Takes in a string and removes all references and returns a string
'''
def removeReferences(textDoc):
	removingReferencesPattern = r'[\[\d\]]'
	updatedTextDoc = re.sub(removingReferencesPattern,"", textDoc)
	return updatedTextDoc

#Removing Alphanumeric characters
def removeAlphanumericCharacters(textDoc):
	updatedTextDoc = re.sub("[^\w]", " ",  textDoc)
	return updatedTextDoc
#caseFolding 
def caseFolding(textDoc):
	updatedTextDoc = textDoc.lower()
	return updatedTextDoc
#Tokenisation of words 
def wordTokenisation(textDoc):
	wordTokens  = word_tokenize(textDoc)
	return wordTokens

#Stopword removal 
def stopWordsRemoval(wordTokens):
	updatedWordTokens = []
	stopWords = set(stopwords.words("english"))
	for w in wordTokens:
		if w not in stopWords: 
			updatedWordTokens.append(w)
	return updatedWordTokens
	
#Function for stemming
def tokenStemming(wordTokens):
	stemmer = PorterStemmer()
	updatedWordTokens = []
	for tokens in wordTokens:
		updatedWordTokens.append(stemmer.stem(tokens))
	return updatedWordTokens 

#Function for lemmatization 
def tokenLemmatization(wordTokens):
	lemmatizer = WordNetLemmatizer()
	updatedWordTokens = []
	for tokens in wordTokens:
		updatedWordTokens.append(lemmatizer.lemmatize(tokens))
	return updatedWordTokens
''''
#Test
textDoc = "The lazy fox is running and ran and runs[18]. !"
print(removeReferences(textDoc))
print("--removing alphanumeric characters---")
print(removeAlphanumericCharacters(textDoc))
print("--casefolding---")
print(caseFolding(textDoc))
print("-----wordTokenisation-----")
tokens = wordTokenisation(textDoc)
print(tokens)
print("-----stop words removal--------")
print(stopWordsRemoval(tokens))
print("-------tokenStemming------")
print(tokenStemming(tokens))
print("-------tokenLemmatization------")
print(tokenLemmatization(tokens))
print("--------tying it all together-------")
updatedTextDoc = removeReferences(textDoc)
updatedTextDoc = removeAlphanumericCharacters(updatedTextDoc)
updatedTextDoc = caseFolding(updatedTextDoc)
newTokens = wordTokenisation(updatedTextDoc)
newTokens = stopWordsRemoval(newTokens)
newTokens = tokenStemming(newTokens)
newTokens = tokenLemmatization(newTokens)
print(newTokens)

invertedIndex = {}
for w in newTokens: 
	if w not in invertedIndex.keys():
		attributesList = []
		#print(type(attributesList))
		attributesList.append(newTokens.index(w))
		attributesList.append(1)		
		invertedIndex[w] = attributesList
	else:
		invertedIndex[w][1] += 1  
'''
def createInvertedIndexWithWordCount(wordTokens):
	invertedIndex = {}
	for w in wordTokens: 
		if w not in invertedIndex.keys():
			attributesList = []
			#print(type(attributesList))
			#attributesList.append(wordTokens.index(w))
			attributesList.append(1)		
			invertedIndex[w] = attributesList
		else:
			invertedIndex[w][0] += 1 
	return invertedIndex

def createInvertedIndexWithLocation(wordTokens):
	invertedIndex = {}
	for w in wordTokens: 
		if w not in invertedIndex.keys():
			attributesList = []
			#print(type(attributesList))
			attributesList.append("")	
			invertedIndex[w] = attributesList
		if w in invertedIndex.keys():
			index_pos_list = 0
			index_pos_list = [ i for i in range(len(wordTokens)) if wordTokens[i] == w ]
			invertedIndex[w].append(index_pos_list)	
	return invertedIndex

infilePath = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.1.txt"
wordDoc = readFile(infilePath)
wordDoc = removeReferences(wordDoc)
wordDoc = removeAlphanumericCharacters(wordDoc)
wordDoc = caseFolding(wordDoc)
wordTokens = wordTokenisation(wordDoc)
wordTokens = stopWordsRemoval(wordTokens)
wordTokens = tokenStemming(wordTokens)
wordTokens = tokenLemmatization(wordTokens)
#invertedIndex = createInvertedIndexWithWordCount(wordTokens)
def sortIndex(invertedIndex):
	sortedDict = {}
	sortedKeys = sorted(invertedIndex, key=invertedIndex.get)
	for w in sortedKeys:
		sortedDict[w] = invertedIndex[w]
	return(sortedDict)	

invertedIndex = createInvertedIndexWithLocation(wordTokens)
print(invertedIndex)   	

