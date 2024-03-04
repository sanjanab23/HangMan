import random
import string

def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "game", "learning"]
    return random.choice(words)

def initialize_display_word(word):
    return "_" * len(word)

def update_display_word(word, display, letter):
    new_display = ""
    for i in range(len(word)):
        if word[i] == letter:
            new_display += letter
        else:
            new_display += display[i]
    return new_display

def draw_hangman(attempts):
    hangman_art = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """
    ]
    print(hangman_art[attempts])

def hangman():
    word = choose_word()
    display = initialize_display_word(word)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print("Guess the word:", display)

    while True:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        elif guess not in string.ascii_lowercase:
            print("Please enter a valid letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            display = update_display_word(word, display, guess)
            print("Correct guess:", display)
        else:
            attempts += 1
            draw_hangman(attempts)
            print("Incorrect guess. Attempts remaining:", max_attempts - attempts)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break
        elif attempts >= max_attempts:
            print("Sorry, you've run out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
