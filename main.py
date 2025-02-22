from stats import get_num_words, get_character_occurence, break_down_counts
from pprint import pprint
import sys



def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {get_num_words(book_path)} total words\n")
    print("--------- Character Count -------\n")

    for count in break_down_counts(get_character_occurence(book_path)):
        for key, value in count.items():
            print(f"{key}: {value}\n")

    print("============= END ===============\n")


main()
