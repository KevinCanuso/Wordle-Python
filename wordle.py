from words import get_random_word, is_valid_word
from check import check_guess

def play_wordle():
    secret_word = get_random_word()
    attempts = 6  # Number of attempts
    
    print("Welcome to the 5-letter Word Guessing Game!")
    print("You have 6 attempts to guess the word.")

    attempt = 0

    while attempt < attempts:
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").strip().lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if not is_valid_word(guess):  # Check if the word exists in words.txt
            print("Invalid word. Please enter a valid 5-letter word.")
            continue

        result = check_guess(guess, secret_word)
        print(" ".join(result))  # feedback

        if guess == secret_word:
            print("Congratulations! You guessed the word correctly.")
            return
        
        attempt += 1

    print(f"Game Over! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    play_wordle()
