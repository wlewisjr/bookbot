from stats import get_word_count
from stats import get_character_count
from stats import sort_characters_by_count

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def print_report(book_path, word_count, sorted_characters_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    count = get_word_count(text)
    char_count = get_character_count(text)
    sorted_analysis = sort_characters_by_count(char_count)
    print_report(book, count, sorted_analysis)

main()
