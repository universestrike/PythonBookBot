from stats import get_word_count
from stats import get_char_count

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def pretty_print(filepath, words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted(chars):
        print(f"{char}: {chars[char]}")

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    words = get_word_count(text)
    chars = get_char_count(text)
    pretty_print(filepath, words, chars)


if __name__ == '__main__':
    main()