from stats import get_word_count, char_count, sort_dict_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main(argv): 
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        print("============ BOOKBOT ============")
        path = argv[1]
        full_book = get_book_text(path)
        print(f"Analyzing book found at {path}")

        print("----------- Word Count ----------")
        num_words = get_word_count(full_book)
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        all_character_count = char_count(full_book)
        sorted_list = sort_dict_list(all_character_count)
        for dict in sorted_list:
            print(f"{dict['char']}: {dict['num']}")
        print("============= END ===============")
        
main(sys.argv)