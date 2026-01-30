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

def show_hand(player, hand):
    """displays the hand of the specified players"""
    print(f"{player} hand: ", [str(card) for card in hand])


#hit or stand

#calculate score
def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        if card.rank in {Rank.Jack, Rank.Queen, Rank.King}:
            score += 10
        elif card.rank ==Rank.Ace:
            score += 11
            aces += 1
        else:
            score += int(card.rank.value)
        
    #adjust for aces if bust
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score
#compare and/or determine winner

#append score to results

#Debug/Testing Should only output if this file is executed directly
if __name__ == "__main__":
    print("Initial deck:")
    for card in deck[:10]:
        print(card)
    print(f"Total cards in deck: {len(deck)}")

    # test shuffle to ensure deck order changes
    print("\n------------------------Testing shuffle------------------------")

    shuffle_deck(deck)

    print("\nShuffled deck:")
    for card in deck[:10]:
        print(card)

    print("\n------------------------Testing dealing------------------------")

    # define player and dealer hands, call deal_hand function to deal 2 cards each
    player_hand = deal_hand(deck, 2)
    dealer_hand = deal_hand(deck, 2)
    
    print()
    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand)
    
    print("\n------------------------Testing calculate_score------------------------")
    # Tests that the cards total to the expected score.
    # Score tests are isolated and only run when this file is executed directly
    test_cases = [
        ([Card(Rank.Ace, Suit.Spades), Card(Rank.Nine, Suit.Hearts)], 20),
        ([Card(Rank.Ace, Suit.Spades), Card(Rank.Ace, Suit.Hearts), Card(Rank.Nine, Suit.Diamonds)], 21),
        ([Card(Rank.King, Suit.Clubs), Card(Rank.Queen, Suit.Spades)], 20),
        ([Card(Rank.Ace, Suit.Spades), Card(Rank.Ace, Suit.Hearts), Card(Rank.Ace, Suit.Diamonds)], 13),
    ]

    for hand, expected in test_cases:
        score = calculate_score(hand)
        print(
            f"Hand: {[str(card) for card in hand]} "
            f"| Score: {score} "
            f"| Expected: {expected}"
        )
        assert score == expected, "❌ Score test failed"

    print("✅ All score tests passed!")
    # test to ensure cards are removed from the deck
    print(f"\nCards left in deck: {len(deck)}")
