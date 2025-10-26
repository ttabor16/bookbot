from stats import (
    get_num_words,
    character_count,
    sorted_list,
)
import sys

def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    character_list = sorted_list(character_count(text))
    print_report(book_path, words, character_list)

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for i in chars_sorted_list:
        print(f"{i['char']}: {i['num']}")
    print("============ END ============")
    
main()