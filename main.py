

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"REPORT OF: {book_path}")
    print(f"There are {num_words} words in the book.")
   
    report_letters_alph(num_letters)
    report_letters_num(num_letters)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    from string import ascii_lowercase as alph
    lower_text = text.lower()
    
    counter = 0
    dictionary = {}

    for char in alph:
        for letter in text:
            if char == letter:
                counter += 1
        dictionary[char] = counter
        counter = 0

    letter_list = list(dictionary.items())
    return letter_list
    
''' solution from boot.dev - much more elegant

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

'''

def report_letters_alph(input_list):
    print("""
Here are the counts of letters in alphabetical order:
----------------------------------------------------------------
    """)
    for item in input_list:
        letter = item[0]
        count = item[1]
        print(f"The letter '{letter}' was found {count} times.")


def report_letters_num(input_list):
    print("""
Here are the counts of letters in descending order of occurence:
----------------------------------------------------------------
    """)

    input_list.sort(key=lambda x: x[1], reverse=True)

    for item in input_list:
        letter = item[0]
        count = item[1]
        print(f"The letter '{letter}' was found {count} times.")

main()