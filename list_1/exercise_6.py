import utility
import itertools
import nltk 
import pdb
from nltk.corpus import stopwords as nltk_stopwords
import string
from preprocessing import preprocess_text


def get_text_file_as_list():
    with open('shrek.txt') as file: 
        return [line for line in file]


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
    chapters = utility.split_by_delimiter(book, "#" * 10)
    preprocessed_chapters = [preprocess_text(chapter) for chapter in chapters]
    pdb.set_trace()
    # pairs = create_pairs(words)
    # grouped_words = group_words(pairs)

