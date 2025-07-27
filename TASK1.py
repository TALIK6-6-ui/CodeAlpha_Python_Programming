import random
import string

# Predefined word list
WORDS = ["python", "hangman", "challenge", "coding", "random"]
MAX_INCORRECT = 6
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""", """
     +---+
     O   |
         |
         |
        ===""", """
     +---+
     O   |
     |   |
         |
        ===""", """
     +---+
     O   |
    /|   |
         |
        ===""", """
     +---+
     O   |
    /|\  |
         |
        ===""", """
     +---+
     O   |
    /|\  |
    /    |
        ===""", """
     +---+
     O   |
    /|\  |
    / \  |
        ==="""
]


def choose_word():
    return random.choice(WORDS)


def display_hangman(incorrect):
    print(HANGMAN_PICS[incorrect])


def display_word_state(word, guessed):
    return ' '.join([c if c in guessed else '_' for c in word])


def get_valid_guess(guessed):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single alphabetical character.")
        elif guess in guessed:
            print("You've already guessed that letter.")
        else:
            return guess


def play_round():
    word = choose_word()
    guessed = set()
    incorrect = 0

    print("\nNew game started!")
    while incorrect < MAX_INCORRECT:
        display_hangman(incorrect)
        print("Word:", display_word_state(word, guessed))
        print(f"Guessed: {', '.join(sorted(guessed))}")
        print(f"Remaining attempts: {MAX_INCORRECT - incorrect}")

        guess = get_valid_guess(guessed)
        guessed.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(c in guessed for c in word):
                print("\nCongratulations! You've guessed the word:", word)
                return True
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect += 1

    # Game over
    display_hangman(incorrect)
    print("\nGame over! The word was:", word)
    return False


def main():
    print("Welcome to Hangman!")
    while True:
        win = play_round()
        again = input("Play again? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == '__main__':
    main()
