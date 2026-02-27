#Enum gives us the ability to store our card suits as the name instead of the icon.
from enum import Enum
#Dataclass allows python to automatically generate init and repr 
from dataclasses import dataclass
#Import random module to allow us to use random methods
import random
#Import datetime to allow tracking of game date and times
from datetime import datetime

results = []
player_points = 0
dealer_points = 0

#deck of cards
class Suit(Enum):
    Spades = "♠"
    Hearts = "♥"
    Diamonds = "♦"
    Clubs = "♣"
class Rank(Enum):
    Ace = "A"
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Ten = "10"
    Jack = "J"
    Queen = "Q"
    King = "K"

#Makes the object immutable so the card cannot be changed after assignment
@dataclass(frozen=True)

class Card:
    rank:Rank
    suit:Suit

    def __str__(self):
        return f"{self.rank.value}{self.suit.value}"

def create_deck():
    return [Card(rank, suit) for suit in Suit for rank in Rank]

#Shuffle deck
def shuffle_deck(deck):
    """
    Use random shuffle method to shuffle the deck.
    This method changes the original list and does not return a new list.
    """
    random.shuffle(deck)


#Deal cards
 
def deal_card(deck):
    """pop method removes and returns the last card from the deck"""
    return deck.pop()


def deal_hand(deck, num_cards):
    hand = []
    """loops for the number of cards specified.
     Calls deal card function and appends dealt cards to the hand"""
    for _ in range(num_cards):
        hand.append(deal_card(deck))
    return hand

def show_hand(player, hand, hide_first=False):
    """displays the hand of the specified players"""
    if hide_first:
        displayed = ["??"] + [str(card) for card in hand[1:]]
    else:
        displayed = [str(card) for card in hand]
        
    print(f"{player}'s hand: {displayed}")

def save_result(player_score, dealer_score, winner):
    """saves the result of the game to a text file with a timestamp"""
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("results.txt", "a") as file:
        file.write(f"{timestamp} Player: {player_score}, Dealer: {dealer_score}, Winner: {winner}\n")

def calculate_score(hand):
    """calculates the score of a hand"""

    score = 0
    aces = 0

    for card in hand:
        if card.rank in [Rank.Jack, Rank.Queen, Rank.King]:
            score += 10
        elif card.rank == Rank.Ace:
            score += 11
            aces += 1
        else:
            score += int(card.rank.value)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score

def calculate_winner(player_hand, dealer_hand):
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"\nFinal Scores: Player {player_score}, Dealer {dealer_score}")

    if player_score > 21:
        return "dealer", "Dealer wins! Player busts."
    elif dealer_score > 21:
        return "player", "Player wins! Dealer busts."
    elif player_score > dealer_score:
        return "player", "Player wins!"
    elif dealer_score > player_score:
        return "dealer", "Dealer wins!"
    else:
        return "tie", "It's a tie!"
    
def run_tests():
    print("Running tests...")
    
    print("\nInitial deck:")
    test_deck = create_deck()
    for card in test_deck[:10]:
        print(card)
    print(f"Total cards in deck: {len(test_deck)}")

        # test shuffle to ensure deck order changes
    print("\n------------------------Testing shuffle------------------------")

    shuffle_deck(test_deck)

    print("\nShuffled deck:")
    for card in test_deck[:10]:
        print(card)

    print("\n------------------------Testing dealing------------------------")

    # define player and dealer hands, call deal_hand function to deal 2 cards each
    player_hand = deal_hand(test_deck, 2)
    dealer_hand = deal_hand(test_deck, 2)
    
    print()
    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand)
    
    # test to ensure cards are removed from the deck
    print(f"\nCards left in deck: {len(test_deck)}")


def play_game():
    print("\nStarting Blackjack Game!")
    deck = create_deck()
    shuffle_deck(deck)

    print("\nShuffling deck...")
    shuffle_deck(deck)
   
    # Deal initial hands
    player_hand = deal_hand(deck, 2)
    dealer_hand = deal_hand(deck, 2)

    print("\nInitial hands:")
    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand, hide_first=True)

    # -------- Player Turn --------
    while True:
        player_score = calculate_score(player_hand)
        print(f"\nPlayer score: {player_score}")

        if player_score > 21:
            print("Player busts! Dealer wins.")
            break

        move = input("Hit or stand: ").lower()
        if move == "hit":
            player_hand.append(deal_card(deck))
            show_hand("Player", player_hand)
        else:
            break
            
    # If player busts, skip dealer turn
    if calculate_score(player_hand) <= 21:

        # -------- Dealer Turn --------
        print("\nDealer reveals:")
        show_hand("Dealer", dealer_hand)

        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            show_hand("Dealer", dealer_hand)

    # -------- Determine Winner --------
    # outcome = calculate_winner(player_hand, dealer_hand)
    # print(outcome)
    # results.append(outcome)

    global player_points, dealer_points

    winner, message = calculate_winner(player_hand, dealer_hand)
    print(message)

    if winner == "player":
        player_points += 1
    elif winner == "dealer":
        dealer_points += 1

    results.append(message)

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    save_result(player_score, dealer_score, winner)

    # print(f"\nResults so far:", results)
    print(f"\nCurrent Score - Player: {player_points}, Dealer: {dealer_points}")    

if __name__ == "__main__":
    run_tests()

    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()

        if again != 'y':
            print("Game over. Thanks for playing!")
            break