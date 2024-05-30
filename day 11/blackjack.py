import random
from replit import clear


# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.
# game starts here:

'_______________________________________________Game Logic_______________________________________________________'
# a function to give random card
def deal_card():
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    random_card = random.randint(0, 12)
    return cards[random_card]

# function  that takes a List of cards as input and returns the score.
def calculate_score(cards):
    total = 0
    if 10 in cards or 'Q' in cards or 'J' in cards or 'K' in cards:
        if 'A' in cards and len(cards) == 2:
            return 0
    for i in cards:
        if i == 'A':
            total += 11
        elif i == 'J' or i == 'Q' or i == 'K':
            total += 10
        else:
            total += i
    if 'A' in cards and total > 21:
        total -= 10

    return total

def compare(user, dealer):
    if user > 21:
        return "Busted! 🫣"
    elif user == dealer:
        return "It's a Draw 🙃"
    elif user == 0:
        return "You Win with a BlackJack 😎"
    elif dealer == 0:
        return "You lost for a BlackJack🫣"
    elif user > 21:
        return "Busted! 🫣"
    if dealer > 21:
        return "Dealer Busted! 🫣, You Win 😎"
    elif user > dealer:
        return "You Win 😎"
    else:
        return "You lost 🫣"
'_________________________Game_____________________________'

def play_game():
    # user and computer variables
    print("""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    useer_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    while is_game_over is not True:

        useer_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your Cards {user_cards}, Current Score {useer_score}")
        print(f"Dealer's First card  {dealer_cards[0]}")

        if useer_score == 0 or dealer_score == 0 or useer_score >= 21:
            is_game_over = True
        else:
            uc = input("Type 'Y' if to Deal and 'N' to Pass: ")
            user_should_deal = uc.lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17 and useer_score <= 21:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand was {user_cards} with a score of {useer_score}")
    print(f"dealer's final hand was {dealer_cards} with a score of {dealer_score}")
    print(compare(useer_score, dealer_score))


while input("Do You Want To Play A Game Of BlackJack!!!? \nType 'Y' or 'N' : ").lower() == 'y':
    clear()
    play_game()
