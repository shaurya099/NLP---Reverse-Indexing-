import re
import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
class InvertedIndex:
    def __init__(self):
        self.textDoc = []
        self.wordTokens = []
        self.invertedIndex = {}
        self.episodeList = [3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,"3.10",3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,"3.20",3.21,3.22,3.23,3.24,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,"4.10",4.11,4.12,4.13,4.14,4.15,4.16,4.17,4.18,4.19,"4.20",4.21,4.22]

    def read_data(self, path: str):
        """
        Read files from a directory and then append the data of each file into a list.
        """
        with open(path) as infile:
            self.textDoc= infile.read()
        infile.close()
        
    
    def remove_References(self):
        removingReferencesPattern = r'[\[\d\]]'
        self.textDoc = re.sub(removingReferencesPattern,"", self.textDoc)
        
    
    def remove_Edit_Blocks(self):
        removeEditBlocksPattern = r'\[edit\]'
        self.TextDoc = re.sub(removeEditBlocksPattern,"", self.textDoc)
       
    
    def remove_Non_Alpha_Numeric_Characters(self):
        self.textDoc = re.sub("[^\w]", " ",  self.textDoc)
        
    
    def case_Folding(self):
        self.textDoc = self.textDoc.lower()
    
    def word_Tokenisation(self):
        self.wordTokens = word_tokenize(self.textDoc)
        #print("tokenizationDone")
    
    def stop_words_Removal(self):
        tempList = []
        stopWords = set(stopwords.words("english"))
        #print("set")
        for w in self.wordTokens:
            if w not in stopWords: 
                tempList.append(w)
        self.wordTokens = tempList
        #print("stopword removal done")
        
    def tokenStemming(self):
        stemmer = PorterStemmer()
        tempList = []
        for tokens in self.wordTokens:
            tempList.append(stemmer.stem(tokens))
        self.workTokens = tempList
        #print("stemming done")
    
    def tokenLemmatization(self):
        tempList = []
        lemmatizer = WordNetLemmatizer()
        for tokens in self.wordTokens:
            tempList.append(lemmatizer.lemmatize(tokens))
        self.wordTokens = tempList
        #print("lemmatization done")
    def process_document(self) -> list:
        """
        pre-process a document and return a list of its terms
        str->list"""
        self.remove_References()
        self.remove_Edit_Blocks()
        self.remove_Non_Alpha_Numeric_Characters()
        self.case_Folding()
        #print("casefolding done")
        self.word_Tokenisation()
        self.stop_words_Removal()
        self.tokenStemming()
        self.tokenLemmatization()
        return(self.wordTokens)
    '''
    def generate_Inverted_Index_With_Word_Count(self):
        for w in self.wordTokens:
            if w not in self.invertedIndex.keys():
                self.invertedIndex[w] =[]
            
            for position, item in enumerate(self.wordTokens):
                episodeString = "{} : {}"
                if item in iself.invertedIndex.keys():
                    self.invertedIndex[item].append(episodeString.format(episode,position))
                else:
                    self.invertedIndex[item] =[]    
                    self.invertedIndex[item].append(episodeString.format(episode,position))
        self.wordTokens = []
    '''            
    
    def index_corpus(self, episode) -> None:
        """
        index given documents
        list->None"""
        for w in self.wordTokens:
            if w not in self.invertedIndex.keys():
                self.invertedIndex[w] =[]
            
            for position, item in enumerate(self.wordTokens):
                episodeString = "{} : {}"
                if item in self.invertedIndex.keys():
                    self.invertedIndex[item].append(episodeString.format(episode,position))
                else:
                    self.invertedIndex[item] =[]    
                    self.invertedIndex[item].append(episodeString.format(episode,position))
        self.wordTokens = []
        
     
    def proximity_search(self, term1: str, term2: str) -> dict:
        """
        1) check whether given two terms appear within a window
        2) calculate the number of their co-existance in a document
        3) add the document id and the number of matches into a dict
        return the dict"""

def main():
    "main call function"
    index = InvertedIndex()# initilaise the index
    for episode in index.episodeList:
        #print(episode)
        pathString = "/Users/shaurya/coding-projects/NLP---Reverse-Indexing-/Simpsons/{}.txt"
        corpus = index.read_data(pathString.format(episode))
        index.process_document()
        index.index_corpus(episode) # index documents/corpus
    print(index.invertedIndex)
    #return index.invertedIndex
main()
