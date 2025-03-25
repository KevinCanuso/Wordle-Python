def check_guess(guess, secret_word):
    feedback = ["\033[37m⬜\033[0m"] * 5  # Default feedback (gray box, white text)

    # Convert words into lists for easier checking
    secret_list = list(secret_word)
    
    # Check correct positions (green)
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = "\033[32m🟩\033[0m"  # Green

    # Check misplaced letters (yellow)
    for i in range(5):
        if guess[i] in secret_list and feedback[i] == "\033[37m⬜\033[0m":
            feedback[i] = "\033[33m🟨\033[0m"  # Yellow
            secret_list[secret_list.index(guess[i])] = None  # Mark as used

    return feedback
