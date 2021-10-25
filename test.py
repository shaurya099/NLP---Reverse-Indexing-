# -*- coding: utf-8 -*-
'''
 Write a function that will read the files from one text document and then create a dictionary in the form of: 
 {word, frequency, document ID} 

The first line of the document is always the title, you can use that as document id
exclude all tags such as 

From Wikipedia, the free encyclopedia
Jump to navigationJump to search
remove references September 19, 1991 [1] - so removing the [1]

Guest appearances
Original air date
Episode features
Episode chronology
← Previous
Next →
List of episodes
Contents
1	Plot
2	Production
2.1	Alternate opening
3	Unproduced sequel
4	Cultural references
5	Reception
6	Reruns
6.1	Pull from circulation
7	References
8	External links
Plot
Production
Reception
 '''
unwantedTags = ["From Wikipedia, the free encyclopedia" , "Jump to navigationJump to search", "Guest appearances", "Original air date", "Original air date", "Episode features" , "Episode chronology", "← Previous" , "Next →" , "List of episodes", "Contents" , "1	Plot", "2	Production" , "2.1	Alternate opening" , "3	Unproduced sequel","4	Cultural references" , "5	Reception", "6	Reruns" , "6.1	Pull from circulation" , "7	References","8	External links","Plot","Production","Reception"]


infilePath = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.2.txt"
outfilePath = "/Users/shaurya/coding-projects/testOutput"

with open(infilePath) as infile, open(outfilePath, "w") as outfile:
	copy = True 
	for line in infile:
		if line.strip() in unwantedTags:
			copy = False 
			continue 
		else:
			outfile.write(line)
infile.close()
outfile.close()
