from wordcloud import WordCloud
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
    
    wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
    wc.generate_from_frequencies(dict(grouped_words[15:]))
    wc.to_file('clouds/book.png')
    pdb.set_trace()