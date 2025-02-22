def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

main()
