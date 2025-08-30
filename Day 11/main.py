from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    user_hand = [choice(cards), choice(cards)]
    dealer_hand = [choice(cards), choice(cards)]

    print(f"Your hand: {user_hand}\nSum: {sum(user_hand)}")
    print(f"Dealer hand: [?, {dealer_hand[1]}]")

    game_over = False

    if sum(dealer_hand) == 21 and sum(user_hand) == 21:
        print("Draw! You both got blackjack")
        game_over = True
    elif sum(dealer_hand) == 21:
        print(f"You lose! Dealer got blackjack\n{dealer_hand}")
        game_over = True
    elif sum(user_hand) == 21:
        print("Blackjack, you win!")
        game_over = True

    while not game_over:
        hit_or_stay = input("Do you want to 'hit' or 'stay'?: ").lower()

        if hit_or_stay == 'hit':
            user_hand.append(draw_card())
            if sum(user_hand) > 21:
                if 11 in user_hand:
                    for index, card in enumerate(user_hand):
                        if user_hand[index] == 11:
                            user_hand[index] = 1
                            print(f"Your hand: {user_hand}\nSum: {sum(user_hand)}")
                            break
                else:
                    print(f"You bust: {sum(user_hand)}\nDealer: {sum(dealer_hand)}")
                    game_over = True
            elif sum(user_hand) == 21:
                print(f"You win! {sum(user_hand)}\nDealer: {sum(dealer_hand)}")
                game_over = True
            else:
                print(f"Your hand: {user_hand}\nSum: {sum(user_hand)}")
        elif hit_or_stay == 'stay':
            while sum(dealer_hand) < 21 and sum(dealer_hand) < sum(user_hand):
                dealer_hand.append(draw_card())
            if sum(dealer_hand) > sum(user_hand) and sum(dealer_hand) <= 21:
                print(f"You lose!\nYour hand: {sum(user_hand)}\nDealer hand: {sum(dealer_hand)}")
            elif sum(user_hand) > sum(dealer_hand) or sum(dealer_hand) > 21:
                print(f"You win!\nYour hand: {sum(user_hand)}\nDealer hand: {sum(dealer_hand)}")
            else:
                print(f"You draw!\nYour hand: {sum(user_hand)}\nDealer hand: {sum(dealer_hand)}")
            game_over = True

    play_again = input("Do you wish to play again? (y/n): ").lower()
    if play_again == 'y':
        blackjack()


def draw_card():
    return choice(cards)

blackjack()
