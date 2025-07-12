import random

def hangman():
    words = ["cpu", "motherboard", "Harddisk", "ram", "keyboard", "mouse"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    word_progress = ["_"] * len(secret_word)

    print("Welcome to Hangman!\n")
    print(" ".join(word_progress))
    print(f"Attempts left: {attempts}")

    while attempts > 0 and "_" in word_progress:
        guess = input("\nEnter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[i] = guess
            print("\nCorrect!")
        else:
            attempts -= 1
            print(f"\nIncorrect! Attempts left: {attempts}")
            
        
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    # Game outcome
    if "_" not in word_progress:
        print("\nCongratulations! You won!")
    else:
        print("\nGame over! You lost!")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    hangman()