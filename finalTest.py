import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import OrderedDict
from more_itertools import locate

'''
ReadFile(infilePath) -> removeReferences(textDoc) -> removeAlphanumericCharacters(textDoc) -> caseFolding(textDoc) _> wordTokenisation(textDoc) -> stopWordsRemoval(wordTokens)-> createInvertedIndexWithWordCount -> sortIndex(invertedIndex)-> createInvertedIndexWithLocation(tokens)
'''

infilePath = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.3.txt" 
infilePath2 = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.2.txt" 

def readFile(infilePath):
	textDoc = " "
	with open(infilePath) as infile:
 		textDoc= infile.read()
	infile.close()
	return textDoc 

def removeReferences(textDoc):
	removingReferencesPattern = r'[\[\d\]]'
	updatedTextDoc = re.sub(removingReferencesPattern,"", textDoc)
	return updatedTextDoc

def removeEditBlocks(textDoc):
	removeEditBlocksPattern = r'\[edit\]'
	updatedTextDoc = re.sub(removeEditBlocksPattern,"", textDoc)
	return updatedTextDoc

def removeAlphanumericCharacters(textDoc):
	updatedTextDoc = re.sub("[^\w]", " ",  textDoc)
	return updatedTextDoc

def caseFolding(textDoc):
	updatedTextDoc = textDoc.lower()
	return updatedTextDoc

def wordTokenisation(textDoc):
	wordTokens  = word_tokenize(textDoc)
	return wordTokens

def stopWordsRemoval(wordTokens):
	updatedWordTokens = []
	stopWords = set(stopwords.words("english"))
	for w in wordTokens:
		if w not in stopWords: 
			updatedWordTokens.append(w)
	return updatedWordTokens

def tokenStemming(wordTokens):
	stemmer = PorterStemmer()
	updatedWordTokens = []
	for tokens in wordTokens:
		updatedWordTokens.append(stemmer.stem(tokens))
	return updatedWordTokens 

def tokenLemmatization(wordTokens):
	lemmatizer = WordNetLemmatizer()
	updatedWordTokens = []
	for tokens in wordTokens:
		updatedWordTokens.append(lemmatizer.lemmatize(tokens))
	return updatedWordTokens

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
			invertedIndex[w] = None 
	for w in invertedIndex.keys():	
		index_pos_list = list(locate(wordTokens, lambda a: a == w))
		invertedIndex[w] = index_pos_list
	return invertedIndex

def sortIndex(invertedIndex):
	sortedDict = {}
	sortedKeys = sorted(invertedIndex, key=invertedIndex.get)
	for w in sortedKeys:
		sortedDict[w] = invertedIndex[w]
	return(sortedDict)	

def createWordCountIndex(infilePath):
	textDoc = readFile(infilePath)
	textDoc = removeReferences(textDoc)
	textDoc = removeAlphanumericCharacters(textDoc)
	textDoc = caseFolding(textDoc)
	wordTokens= wordTokenisation(textDoc)
	wordTokens = stopWordsRemoval(wordTokens)
	wordTokens= tokenStemming(wordTokens)
	wordTokens = tokenLemmatization(wordTokens)
	invertedIndex = createInvertedIndexWithWordCount(wordTokens)
	invertedIndex = sortIndex(invertedIndex)
	return invertedIndex

def createInvertedIndex(infilePath):
	textDoc = readFile(infilePath)
	textDoc = removeReferences(textDoc)
	textDoc = removeAlphanumericCharacters(textDoc)
	textDoc = caseFolding(textDoc)
	wordTokens= wordTokenisation(textDoc)
	wordTokens = stopWordsRemoval(wordTokens)
	wordTokens= tokenStemming(wordTokens)
	wordTokens = tokenLemmatization(wordTokens)
	invertedIndex = createInvertedIndexWithLocation(wordTokens)
	return invertedIndex

#def updateIndexWithWordCount(wordTokens, invertedIndex):
	updatedInvertedIndex = {}
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
	
def generateTokens(infilePath):
	textDoc = readFile(infilePath)
	textDoc = removeReferences(textDoc)
	textDoc = removeEditBlocks(textDoc)
	textDoc = removeAlphanumericCharacters(textDoc)
	textDoc = caseFolding(textDoc)
	wordTokens = wordTokenisation(textDoc)
	wordTokens = stopWordsRemoval(wordTokens)
	wordTokens = tokenStemming(wordTokens)
	wordTokens = tokenLemmatization(wordTokens)
	return wordTokens

inverted_Index = {}
wordTokens = generateTokens(infilePath)
inverted_Index = createInvertedIndexWithWordCount(wordTokens)
print(len(inverted_Index.keys()))
def updateWordCountIndex(infilePath2, invertedIndex):
	tempIndex = createWordCountIndex(infilePath2)
	for w in tempIndex.keys():
		if w in invertedIndex.keys():
			invertedIndex[w][0] += 1
		else: 
			attributesList = []
			attributesList.append(1)
			invertedIndex[w] = attributesList 
	return invertedIndex

inverted_Index = updateWordCountIndex(infilePath2, inverted_Index)
inverted_Index = sortIndex(inverted_Index)
print(inverted_Index)
print(len(inverted_Index.keys()))
