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
        chapter_cloud_data.append((word, weight))
    weight = lambda element: element[1]
    chapter_cloud_data.sort(key=weight, reverse=True)
    return chapter_cloud_data


if __name__ == '__main__':
    book = utility.get_text_file_as_list('shrek.txt')
    chapters = utility.split_by_delimiter(book, "#" * 10)
    preprocessed_chapters = [preprocess_text(chapter) for chapter in chapters]
    data = prepare_word_cloud_data(preprocessed_chapters)
    pdb.set_trace()
    # TODO: generate word clouds!!!
    # TODO: subexercise 5!!!
