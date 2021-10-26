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

text_encode = textDoc.encode(encoding="ascii", errors="replace")
decodedTextDoc = text_encode.decode() 
#print(decodedTextDoc)
#textDoc = text_encode.decode()
punct = set(string.punctuation) 
#textDoc = " ".join([ch for ch in textDoc if ch not in punct])
textDoc= decodedTextDoc.lower()
#patternOne = r'\[[^)]*\]'
patternOne = r'[\[\d\]]'


#print(textDoc)
print("----------")
textDoc = re.sub(patternOne,"", textDoc)
#print(textDoc)
wordlist = re.sub("[^\w]", " ",  textDoc).split()
unwantedTags = ["From Wikipedia, the free encyclopedia" , "Jump to navigationJump to search", "Guest appearances", "Original air date", "Original air date", "Episode features" , "Episode chronology", "← Previous" , "Next →" , "List of episodes", "Contents" , "1	Plot", "2	Production" , "2.1	Alternate opening" , "3	Unproduced sequel","4	Cultural references" , "5	Reception", "6	Reruns" , "6.1	Pull from circulation" , "7	References","8	External links","Plot","Production","Reception", "1", "2", "3", "4", "5", "6", "7", "8"]
newUnwantedTags = []

for tags in unwantedTags:
	tags = tags.lower()
	tags = tags.split()	#creates a list 
	newUnwantedTags.append(tags)


print(wordlist)




