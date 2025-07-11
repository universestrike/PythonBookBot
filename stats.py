def get_word_count(text): 
    wordCount = text.split()
    return len(wordCount)

def get_char_count(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
