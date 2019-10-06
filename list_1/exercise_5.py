import utility
import itertools
import nltk 
import pdb
from nltk.corpus import stopwords as nltk_stopwords
import string
from preprocessing import preprocess_text


def create_pairs(words): 
    return [(word, 1) for word in words]


def group_words(pairs):
    word = lambda pair: pair[0]
    occurences = lambda pair: pair[1]

    pairs.sort()
    words_grouped = [(w, sum(1 for _ in g)) for w, g in itertools.groupby(pairs, key=word)]
    words_grouped.sort(key=occurences, reverse=True)
    return words_grouped


if __name__ == '__main__':
    book = utility.get_text_file_as_list('shrek.txt')
    words = preprocess_text(book)
    pairs = create_pairs(words)
    grouped_words = group_words(pairs)
    utility.save_to_file('shrek_cloud', grouped_words[23:])
    pdb.set_trace()


"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

words = ["game","gaming","gamed","games"]
ps = PorterStemmer()

for word in words:
    print(ps.stem(word))
"""