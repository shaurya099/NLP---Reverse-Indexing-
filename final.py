import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import OrderedDict

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

def sortIndex(invertedIndex):
	sortedDict = {}
	sortedKeys = sorted(invertedIndex, key=invertedIndex.get)
	for w in sortedKeys:
		sortedDict[w] = invertedIndex[w]
	return(sortedDict)	

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

def updateWordCountIndex(infilePath2, invertedIndex):
	wordTokens = generateTokens(infilePath2)
	for w in wordTokens: 
		if w in invertedIndex.keys():
			invertedIndex[w] = invertedIndex[w] + 1
		else:
			invertedIndex[w] = 1
	return invertedIndex		

def createInvertedIndexWithLocation(wordTokens):
	invertedIndex = {}
	for w in wordTokens:
		if w not in invertedIndex.keys():
			invertedIndex[w] =[]

	for position, item in enumerate(wordTokens):
		episodeString = "3.1 : {}"
		invertedIndex[item].append(episodeString.format(position))

	return invertedIndex

def createInvertedIndexWithWordCount(wordTokens):
	invertedIndex = {}
	for w in wordTokens: 
		if w not in invertedIndex.keys():
			invertedIndex[w] = 1	
		else:
			invertedIndex[w] += 1 
	return invertedIndex

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

def main():
	infilePathMain = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.1.txt"
	tokensMain = generateTokens(infilePathMain)
	invertedIndex = createInvertedIndexWithWordCount(tokensMain)


	list_of_episodes  = [3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,"3.10",3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,"3.20",3.21,3.22,3.23,3.24,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,"4.10",4.11,4.12,4.13,4.14,4.15,4.16,4.17,4.18,4.19,"4.20",4.21,4.22]
	for episode in list_of_episodes:
		pathString = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/{}.txt"
		invertedIndex = updateWordCountIndex(pathString.format(episode), invertedIndex)
	
	print(sortIndex(invertedIndex))

def main2():
	infilePathMain = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.1.txt"
	tokensMain = generateTokens(infilePathMain)
	invertedIndex = createInvertedIndexWithLocation(tokensMain)


	list_of_episodes  = [3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,"3.10",3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,"3.20",3.21,3.22,3.23,3.24,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,"4.10",4.11,4.12,4.13,4.14,4.15,4.16,4.17,4.18,4.19,"4.20",4.21,4.22]

	for episode in list_of_episodes:
		pathString = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/{}.txt"
		wordTokens = generateTokens(pathString.format(episode))
		for position, item in enumerate(wordTokens):
			episodeString = "{} : {}"
			if item in invertedIndex.keys():
				invertedIndex[item].append(episodeString.format(episode,position))
			else:
				invertedIndex[item] =[]	
				invertedIndex[item].append(episodeString.format(episode,position))
			
	return invertedIndex
				
invertedIndex = main2()
#word1 = invertedIndex["michael"]
#word2 = invertedIndex["schumaker"]
#print(word1)
print("----------------")
#print(word2)
#print(word1[0].split(":"))

'''
word1: [4.1:23, 4.2:25]
word2:[4.1:24, 4.1:55]
'''
'''
tempWord1 = word1[0].split(":")
print(type(tempWord1[0]))
matchedEpisodes = set()
for i in range(len(word1)): 
	for j in range(len(word2)):
		proximityDifference = 0
		tempWord1 = word1[i].split(":")
		tempWord2 = word2[j].split(":")
		if tempWord1[0] == tempWord2[0]:
			proximityDifference = int(tempWord1[1]) - int(tempWord2[1])
		if abs(proximityDifference) <= 2:
			matchedEpisodes.add(tempWord1[0])
		else: 
			print("no matches found")	
print(matchedEpisodes)
'''
def proximitySearch(invertedIndex, query1, query2):
	word1 = invertedIndex[query1]
	word2 = invertedIndex[query2]
	matchedEpisodes = set()
	for i in range(len(word1)): 
		for j in range(len(word2)):
			proximityDifference = 0
			tempWord1 = word1[i].split(":")
			tempWord2 = word2[j].split(":")
			if tempWord1[0] == tempWord2[0]:
				proximityDifference = int(tempWord1[1]) - int(tempWord2[1])
			if abs(proximityDifference) <= 2:
				matchedEpisodes.add(tempWord1[0])
		
	print(matchedEpisodes)
proximitySearch(invertedIndex,"michael","jackson")

