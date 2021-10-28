def createInvertedIndexWithLocation(wordTokens):
	invertedIndex = {}
	for w in wordTokens:
		if w not in invertedIndex.keys():
			invertedIndex[w] =[]

	for position, item in enumerate(wordTokens):
		episodeString = "3.1 : {}"
		invertedIndex[item].append(episodeString.format(position))

	return invertedIndex
        	
def updateWordCountIndex(infilePath2, invertedIndex,episode):
	tempIndex = createInvertedIndexWithLocation(infilePath2)
	for w in tempIndex.keys():
		if w not in invertedIndex.keys():
			invertedIndex[w] =[]
		else:
			string = {"{} : {} "}
			invertedIndex[w].append()
		
			
		
	return invertedIndex
	
