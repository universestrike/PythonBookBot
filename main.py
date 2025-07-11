from stats import get_word_count

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():

    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    words = get_word_count(text)
    print(f"{words} words found in the document")


if __name__ == '__main__':
    main()