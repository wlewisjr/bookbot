from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print(f"{word_count} words found in the document")
    print(char_count)

main()
