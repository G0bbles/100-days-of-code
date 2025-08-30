from random import choice
from hangman_art import HANGMANPICS
from hangman_words import words

word_to_guess = choice(words)
placeholder = ["_" for _ in range(len(word_to_guess))]
guessed_letters = []
print(word_to_guess)

GAME_OVER = False
LIVES = 6
while not GAME_OVER:
    guess = input("Choose a letter: ").lower()

    if guess in guessed_letters:
        print(HANGMANPICS[LIVES])
        print("You've already guessed that letter, try again.\n"
              f"Guessed Letters: {' '.join(guessed_letters)}")
        print(''.join(placeholder))

    elif not guess.isalpha() or len(guess) != 1:
        print("You need to guess a single letter.")

    elif guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if guess == word_to_guess[i]:
                placeholder[i] = guess
                guessed_letters.append(guess)
        print(HANGMANPICS[LIVES])
        print(''.join(placeholder))

    else:
        LIVES -= 1
        guessed_letters.append(guess)
        print(HANGMANPICS[LIVES])
        print("This letter is not in the word.")
        print(''.join(placeholder))
        if LIVES == 0:
            print("You lose.")
            GAME_OVER = True

    if ''.join(placeholder) == word_to_guess:
        print(HANGMANPICS[LIVES])
        print("You guessed the word!")
        print(''.join(placeholder))
        GAME_OVER = True
    print()
