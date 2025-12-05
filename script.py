#Enum gives us the ability to store our card suits as the name instead of the icon.
from enum import Enum
#Dataclass allows python to automatically generate init and repr 
from dataclasses import dataclass

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

#Debug/Testing Should only output if this file is executed directly
if __name__ == "__main__":
    for card in deck[:10]:
        print(card)
    print(f"Total cards in deck: {len(deck)}")



#deal cards

#hit or stand

#calculate score

#compare and/or determine winner

#append score to results