import matplotlib.pyplot as plt
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS
import utility
import itertools
import nltk 
import pdb
from nltk.corpus import stopwords as nltk_stopwords
import string
from preprocessing import preprocess_text


def prepare_word_cloud_data(chapters):
    return [get_chapter_cloud(chapters, chapter) for chapter in chapters]


def get_chapter_cloud(chapters, chapter):
    chapter_cloud_data = []
    unique_words = set(chapter)
    for word in unique_words:        
        weight = utility.tf_idf(word, chapters, chapter)
        chapter_cloud_data.append((word, int(weight * 100)))
    weight = lambda element: element[1]
    chapter_cloud_data.sort(key=weight, reverse=True)
    return chapter_cloud_data


if __name__ == '__main__':
    book = utility.get_text_file_as_list('shrek.txt')
    chapters = utility.split_by_delimiter(book, "#" * 10)
    preprocessed_chapters = [preprocess_text(chapter) for chapter in chapters]
    cloud_data = prepare_word_cloud_data(preprocessed_chapters)
    
    for i, data in enumerate(cloud_data): 
        wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
        wc.generate_from_frequencies(dict(data[5:]))
        wc.to_file(f'clouds/shrek_cloud{i}.png')

    # subexercise 5
    preprocessed_book = preprocess_text(book)
    cloud = get_chapter_cloud(preprocessed_book, preprocessed_book)
    wc = WordCloud(background_color="white", max_words=2000, contour_width=3, contour_color='steelblue')
    wc.generate_from_frequencies(dict(cloud[15:]))
    wc.to_file('clouds/book_tf_idf.png')

