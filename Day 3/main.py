print("Welcome to treasure island")
choice1 = input("You come to a fork in the path, do you go 'left' or 'right'?\n").lower()
if choice1 == 'left':
    choice2 = input("You come across a river. Do you attempt to 'swim' or 'wait'?\n").lower()
    if choice2 == "wait":
        choice3 = input("You come across three doors. Do you chose 'red', 'blue', or 'yellow'?\n")
        if choice3 == "yellow":
            print("You win!")
        elif choice3 == "red":
            print("You walked into a room full of fire; what did you think red indicated?")
        elif choice3 == "blue":
            print("The room filled with water and sharks. You're now chum.")
        else:
            print('You didn\'t pick a door. You waited, and waited, and waited.'
                  'You waited until death.')
    else:
        print('You attempted to swim. Fish are not friendly in these parts; you\'re now sleeping with the fishies.')
else:
    print('You walked into a pack of bears. Needless to say, you are no longer alive.')
