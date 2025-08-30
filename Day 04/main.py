from random import choice
print("Welcome to Rock, Paper, Scissors")
rps_list = ['rock', 'paper', 'scissors']

USER_SCORE = 0
BOT_SCORE = 0
GAME_OVER = False

while not GAME_OVER:
    user_choice = input("Choose what you will play. Rock, Paper, or Scissors. "
                        "Or use 'quit' to exit.\n").lower()
    bot_choice = choice(rps_list)

    if (user_choice == 'rock' and bot_choice == 'scissors') \
        or (user_choice == 'paper' and bot_choice == 'rock') \
        or (user_choice == 'scissors' and bot_choice == 'paper'):
        USER_SCORE += 1
        print(f"You win! Current Score:\n You - {USER_SCORE}\nBot - {BOT_SCORE}")
    elif user_choice == bot_choice:
        print(f"Draw! Current Score:\n You - {USER_SCORE}\nBot - {BOT_SCORE}")
    elif user_choice == 'quit':
        GAME_OVER = True
        print(f"Final score: \n You - {USER_SCORE}\nBot - {BOT_SCORE}")
    elif user_choice not in rps_list:
        print("You need to choose Rock, Paper, or Scissors.")
    else:
        BOT_SCORE += 1
        print(f"You lost. Current Score:\n You - {USER_SCORE}\nBot - {BOT_SCORE}")
