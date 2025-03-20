from stats import get_num_words
from stats import count_letters 
from stats import sort_character_counts
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
        sys.exit(1)


def main(argv):

    if len(argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 



    book_text = get_book_text(argv[1])

    word_count = get_num_words(book_text)

    char_counts = count_letters(book_text)

    sorted_chars = sort_character_counts(char_counts)

    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Letter Count --------")
	

    # Loop through the sorted characters and print only alphabetic ones
    for char_dict in sorted_chars:
        # Extract character and count from the dictionary
        character = char_dict["char"]
        count = char_dict["count"]

        # Skip non-alphabetic characters
        if character.isalpha():
            print(f"{character}: {count}")        

    print("============= END ===============")

main(sys.argv)
