from stats import get_num_words, get_character_occurence, break_down_counts
from pprint import pprint


def main():
    # get_num_words()

    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print("Found 75767 total words\n")
    print("--------- Character Count -------\n")

    for count in break_down_counts(get_character_occurence()):
        for key, value in count.items():
            print(f"{key}: {value}\n")

    print("============= END ===============\n")


main()
