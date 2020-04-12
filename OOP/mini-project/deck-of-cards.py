from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init(self):
        suits = ["Hearts", "Diamonds", "Clubs", "spades"]
        values = ['A', "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        cards_to_remove = number
        count = self.count()
        actual = min([count, number])
        if count == 0:
            return ValueError "All Cards have been dealt"
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            return ValueError "Only full decks can be shuffled"
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)
