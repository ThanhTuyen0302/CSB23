import random

class Card:
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['heart', 'diamond', 'club', 'spade']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __lt__(self, other):
        # For sorting: suit first, then value
        suit_order = Card.SUITS
        value_order = Card.VALUES
        if suit_order.index(self.suit) != suit_order.index(other.suit):
            return suit_order.index(self.suit) < suit_order.index(other.suit)
        return value_order.index(self.value) < value_order.index(other.value)

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for suit in Card.SUITS for value in Card.VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_a_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None

    def sort(self):
        self.cards.sort()

    def __str__(self):
        card_list = ', '.join(str(card) for card in self.cards)
        return f"Deck of {len(self.cards)} cards:\n{card_list} "
