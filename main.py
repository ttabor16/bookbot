def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    print(f"Found {words} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def word_count(strings):
    words = strings.split()
    return len(words)
    
main()