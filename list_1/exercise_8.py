import pdb
import utility
import preprocessing
import collections
import random
"""
For each given word in your book make a list of five most common words 
that appear directly after considered word (but ignore stop-words). 
Use this summary to generate a random paragraph that resembles a paragraph of your book.
"""

def get_words_with_most_common_successors(book):
    unique_words = set(book)
    return {word: get_most_common_words(word, book) for word in unique_words}


def get_most_common_words(word, book, no_of_words:int=5):
    succeeding_words = create_corpuses(word, book)
    most_common_words_with_number = collections.Counter(succeeding_words).most_common(no_of_words)
    return [element[0] for element in most_common_words_with_number]


def create_corpuses(word, book):
    word_occurence_indices = [index for index, element in enumerate(book) if element.strip() == word]
    return [book[index+2] for index in word_occurence_indices if index+2 < len(book)]


def generate_random_paragraph(start_word, words, length=50):
    next_word = words[start_word][random.randint(0, len(words[start_word])-1)]
    paragraph = [start_word, next_word]

    current_word = next_word

    for _ in range(length-2):
        random_index = random.randint(0, len(words[current_word])-1)
        next_word = words[current_word][random_index]
        current_word = next_word
        paragraph.append(next_word)
    return ' '.join(paragraph)


if __name__ == '__main__':
    book = utility.get_text_file_as_list('shrek.txt')
    book = preprocessing.preprocess_text(book)
    words_with_successors = get_words_with_most_common_successors(book)
    paragraph = generate_random_paragraph('donkey', words_with_successors)
    pdb.set_trace()
