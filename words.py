import random

def load_words():
    """Load words from the words.txt file into a list."""
    try:
        with open("words.txt", "r") as file:
            return [line[:5].lower()
                    for line in file]
    except FileNotFoundError:
        print("Error: words.txt not found. Please add a file with 5-letter words.")
        exit()

WORDS_LIST = load_words()  # Load words once for efficiency

def get_random_word():
    """Get a random 5-letter word from the list."""
    if WORDS_LIST:
        return random.choice(WORDS_LIST) 
    else:
        None

def is_valid_word(word):
    """Check if a word exists in words.txt."""
    return word in WORDS_LIST

