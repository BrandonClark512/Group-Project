#Enum gives us the ability to store our card suits as the name instead of the icon.
from enum import Enum
#Dataclass allows python to automatically generate init and repr 
from dataclasses import dataclass
#Import random module to allow us to use random methods
import random

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

deck = [Card(rank, suit) for suit in Suit for rank in Rank]


#Shuffle deck

#Use random module shuffle method to shuffle the deck. This method takes a sequence and reorders it. It changes the original list and does not return a new list so we can use deck as normal after this.
def shuffle_deck(deck):
    random.shuffle(deck)


#Deal cards

# defines function to deal a card from the deck, passing in the deck as a parameter. 
def deal_card(deck):
    # uses the pop method to remove and return the last card from the deck
    return deck.pop()

# defines function to deal a hand of cards, passing in the deck and number of cards to deal as parameters
def deal_hand(deck, num_cards):
    # starts with an empty list for the hand
    hand = []
    # Loops for the number of cards specified
    for _ in range(num_cards):
        #calls the deal_card function and appends the result to the hand
        hand.append(deal_card(deck))
    # returns the completed hand (must be outside of loop otherwise it will return after the first iteration)
    return hand
    
shuffle_deck(deck)

# define player and dealer hands, call deal_hand function to deal 2 cards each
player_hand = deal_hand(deck, 2)
dealer_hand = deal_hand(deck, 2)

# print hands
print('Player hand: ', [str(card) for card in player_hand])
print('Dealer hand: ', [str(card) for card in dealer_hand])

#hit or stand

#calculate score

#compare and/or determine winner

#append score to results

#Debug/Testing Should only output if this file is executed directly
if __name__ == "__main__":
    for card in deck[:10]:
        print(card)
    print(f"Total cards in deck: {len(deck)}")