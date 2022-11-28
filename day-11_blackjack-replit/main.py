import random as rd
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# sum is easier than this function:)
def total(list_of_cards):
    amount = 0
    for i in list_of_cards:
        amount += i
    return amount


# asking "if 11 in list" easier than for loop
def ace_control(list_of_cards):
    """To check there is a 11"""
    for i in range(len(list_of_cards)):
        if list_of_cards[i] == 11 and total(list_of_cards) > 21:
            list_of_cards[i] = 1


def final(user_cards, dealer_cards):
    print(f"  Your final hand: {user_cards},current score: {total(user_cards)} ")
    print(f"  Computer's final hand: {dealer_cards},current score: {total(dealer_cards)} ")


def compare(user_total, dealer_total):
    if user_total > 21 and dealer_total > 21:
        print("You Lost!")
    elif user_total == 21:
        print("You Win!")
    elif dealer_total == 21:
        print("Black Jack! You Lost!")
    elif user_total > 21:
        print("You Lost!")
    elif dealer_total > 21:
        print("You Win!")
    elif user_total > dealer_total:
        print("You Win!")
    elif dealer_total > user_total:
        print("You Lost!")
    elif user_total == dealer_total:
        print("Draw!")
    else:
        print("You Lost!")


def game():
    user_cards = []
    dealer_cards = []
    for i in range(2):
        user_cards.append(rd.choice(cards))
        dealer_cards.append(rd.choice(cards))
    print(f"  Your cards: {user_cards}, current score: {user_cards[0] + user_cards[1]}")
    print(f"  Computer's first card: {dealer_cards[0]}")

    game_continue = True
    while game_continue:
        # first check for user
        ace_control(user_cards)
        user_total = total(user_cards)
        if user_total == 21:
            print("Black Jack! You Win!")
            game_continue = False
        else:
            response = input("Type \'y\' to get another card, type \'n\' to pass: ")
            if response == "y":
                user_cards.append(rd.choice(cards))
                user_total = total(user_cards)
                print(f"  Your cards: {user_cards}, current score: {user_total}")
                if user_total > 21:
                    print("You Lost!")
                    final(user_cards, dealer_cards)
                    game_continue = False

            if response == "n":
                while total(dealer_cards) < 17:
                    ace_control(dealer_cards)
                    dealer_cards.append(rd.choice(cards))
                dealer_total = total(dealer_cards)
                compare(user_total, dealer_total)
                final(user_cards, dealer_cards)
                game_continue = False

play = True
while play:
    user_choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
    if user_choice == "n":
        play = False
    if user_choice == "y":
        print(logo)
        game()
