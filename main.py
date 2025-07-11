from stats import get_word_count
from stats import get_char_count

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():

    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    words = get_word_count(text)
    chars = get_char_count(text)
    for char in sorted(chars):
        print(f"'{char}': {chars[char]}")


if __name__ == '__main__':
    main()