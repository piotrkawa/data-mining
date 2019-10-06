from typing import List
import pdb

def save_to_file(file_name:str, content: List):
    with open(file_name, 'w') as file:
        for element in content:
            file.write(f'{element[1]} {element[0]} \n')


def get_text_file_as_list(file_path: str):
    with open(file_path, 'r') as file: 
        return [line for line in file]


def split_by_delimiter(iterable, delimiter): 
    """
    Split by delimiter element.
    """
    indices = [index for index, element in enumerate(iterable) if element.strip() == delimiter]
    indices.append(len(iterable))
    indices = indices[1:]
    
    boundaries = []
    for i in range(0, len(indices)-1, 2):  # TODO: rework it!!!
        boundaries.append((indices[i]+1, indices[i+1]))
    return [iterable[boundary[0]:boundary[1]+1] for boundary in boundaries]


def tf_idf():
    ...


def tf():
    ...


def idf():
    ...