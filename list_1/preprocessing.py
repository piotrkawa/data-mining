import nltk 
import pdb
from nltk.corpus import stopwords as nltk_stopwords
import string
import typing
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


str_list = typing.List[str]

def preprocess_text(book: str_list):
    book = remove_whitespaces(book)
    book = remove_punctuation(book)
    book = convert_to_lowercase(book)
    book = ' '.join(book)
    book = tokenize(book)
    book = remove_stopwords(book)
    # book = perform_stemming(book) 
    return book


def remove_whitespaces(book: str_list): 
    book = [line.strip() for line in book]
    book = [line for line in book if line]
    return book
    
    
def convert_to_lowercase(book: str_list):
    return [line.lower() for line in book]


def remove_stopwords(book: str_list):
    stopwords = set(nltk_stopwords.words('english'))
    return [word for word in book if word not in stopwords]


def remove_punctuation(book: str_list):
    return [line.translate(str.maketrans('', '', string.punctuation)) for line in book] 


def tokenize(book: str):
    return nltk.word_tokenize(book) 


def perform_stemming(book):
    ps = PorterStemmer()
    return [ps.stem(word) for word in book]
