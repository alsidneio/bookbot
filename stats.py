from typing import List


def get_num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")


def get_character_occurence() -> dict:
    char_dict = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for char in file_contents:
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    # print(char_dict)
    return char_dict


def sort_on(dict):
    return list(dict.values())[0]


def break_down_counts(char_dict: dict) -> List:
    char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            char_list.append({key: value})

    char_list = sorted(char_list, reverse=True, key=sort_on)

    return char_list
