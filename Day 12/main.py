from random import randint

def difficulty():
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == 'easy':
        return 10
    elif difficulty_choice == 'hard':
        return 5
    else:
        print("You did not enter a valid option.")
        difficulty()

def number_guess_game():
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = randint(1, 100)
    print(number_to_guess)
    lives = difficulty()
    while lives > 0:
        print(f"You have {lives} lives left to guess the number.")
        number_guessed = int(input("Make a guess between 1 and 100: "))
        if number_guessed > number_to_guess:
            print("Too high.")
            lives -=1
        elif number_guessed < number_to_guess:
            print("Too low.")
            lives -=1
        elif number_guessed < 1 or number_guessed > 100:
            print("That's not in the number range.")
        else:
            print("That's correct!")
            break

        if lives == 0:
            print("You did not guess the number correctly")

    continue_game = input("Do you want to play again? (y/n): ").lower()
    if continue_game == 'y':
        number_guess_game()

number_guess_game()
