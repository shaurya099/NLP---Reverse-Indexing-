infilePath = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/3.2.txt"
with open(infilePath) as infile:
	words = ""
	for line in infile:
		words.append(line.strip())

print (words)
