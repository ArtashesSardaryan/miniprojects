'''
About Programm : Hangman Game: Implement the classic word-guessing game, Hangman, where
players try to guess a hidden word one letter at a time. Display the current state
of the word, the letters guessed so far, and allow a limited number of incorrect
guesses before the game ends.

Version : 1.0

Author : Artash
'''
import random

def choose_word():
    '''Function To choose random word from list'''
    words = ["cat", "frog", "tiger", "dog", "horse", "mamont"]
    return random.choice(words)

def display_word(word, guessed_letters):
    '''Function To display Current status'''
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    '''Function hangman game'''
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1
        
    if attempts == 0:
        print("You're out of attempts! The word was:", word)

if __name__ == "__main__":
    
    hangman()