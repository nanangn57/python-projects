############### O 2ur Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_name = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]


def get_card(card, card_name):
    new_card_name = random.choice(cards_name)
    card_name.append(new_card_name)
    card.append(cards[cards_name.index(new_card_name)])
    score = get_score(card)
    return card, card_name, score


def get_score(card):
    if sum(card) > 21 and 11 in card:
        card.remove(11)
        card.append(1)
        score = sum(card)
    else:
        score = sum(card)
    return score


def compare_card(your_score, computer_score):
    if your_score == 21:
        print("BlackJack, your score is 21")
    elif computer_score == 21:
        print("You lose. Computer get BlackJack")
    elif computer_score > 21:
        print(f"You win. Computer card is {computer_card_name}, final score is {computer_score}")
    elif your_score > 21:
        print(f"You lose. You went over. Your card is {your_card_name}, final score is {your_score}")
    elif your_score < computer_score:
        print(f"You lose. Your card is {your_card_name}, final score is {your_score}")
        print(f"Computer card is {computer_card_name}, final score is {computer_score}")
    elif your_score > computer_score:
        print(f"You win. Your card is {your_card_name}, final score is {your_score}")
        print(f"Computer card is {computer_card_name}, final score is {computer_score}")


play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

while play_game == 'y':

    your_card = []
    computer_card = []
    your_card_name = []
    computer_card_name = []

    for i in range(2):
        your_card, your_card_name, your_score = get_card(your_card, your_card_name)
        computer_card, computer_card_name, computer_score = get_card(computer_card, computer_card_name)

    print(f"Your card, {your_card_name}, current_score = {your_score}")
    print(f"Computer first card: {computer_card_name[0]}")
    print(computer_card_name, computer_score)

    game_over = 'n'
    cont = input("Type 'y' to get another card, type 'n' to pass: ")

    while cont == 'y':
        your_card, your_card_name, your_score = get_card(your_card, your_card_name)
        if get_score(your_card) > 21:
            print(f"You went over. Your card is {your_card_name}, your_score is {get_score(your_card)}")
            game_over = 'y'
            break
        else:
            print(f"Your card, {your_card_name}, current_score = {your_score}")

        cont = input("Type 'y' to get another card, type 'n' to pass: ")

    while computer_score < 17:
        computer_card, computer_card_name, computer_score = get_card(computer_card, computer_card_name)
        if computer_score > 21:
            print(f"You win. Computer card is {computer_card_name}, computer score is {get_score(computer_card)}")
            game_over = 'y'
        else:
            pass

    while your_score == computer_score and your_score < 21:
        print("Draw! You must get another card!")
        your_card, your_card_name, your_score = get_card(your_card, your_card_name)

    if game_over == 'n':
        compare_card(your_score, computer_score)

    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
