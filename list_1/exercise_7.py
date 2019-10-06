import pdb

import utility
from preprocessing import preprocess_text


def get_preprocessed_chapters(book_name):
    book = utility.get_text_file_as_list(book_name)
    chapters = utility.split_by_delimiter(book, "#" * 10)
    preprocessed_chapters = [preprocess_text(chapter) for chapter in chapters]
    return preprocessed_chapters


def get_most_matching_chapters(word, chapters):
    chapter_weights = []
    for index, chapter in enumerate(chapters):
        chapter_weight = (index, utility.tf_idf(word, chapters, chapter))
        chapter_weights.append(chapter_weight)
    chapter_weights.sort(key=lambda element: element[1], reverse=True)
    return chapter_weights


if __name__ == '__main__':
    word = 'shrek'
    preprocessed_chapters = get_preprocessed_chapters('shrek.txt')
    chapter_weights = get_most_matching_chapters(word, preprocessed_chapters)
    print(chapter_weights)
    pdb.set_trace()
