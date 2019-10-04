import nltk 
import pdb
from nltk.corpus import stopwords as nltk_stopwords
import string
from preprocessing import preprocess_text

def load_book():
    with open('sherlock-holmes.txt') as file: 
        return [line for line in file]



book = load_book()
book = preprocess_text(book)


pdb.set_trace()


"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

words = ["game","gaming","gamed","games"]
ps = PorterStemmer()

for word in words:
    print(ps.stem(word))
"""