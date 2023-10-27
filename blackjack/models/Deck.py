import random
from models.Card import Card


class Deck:
    def __init__(self):
        self.deck = self.fill_deck()
        self.shuffle_deck()

    def fill_deck(self):
        """fills the deck with a default configuration of cards"""
        new_deck = []
        for suit in ["S", "D"]:
            for value in range(1, 14):
                new_deck.append(Deck.make_new_card(suit, value))
        for suit in ["C", "H"]:
            for value in range(13, 0, -1):
                new_deck.append(Deck.make_new_card(suit, value))
        return new_deck

    def make_new_card(suit, value):
        """helper function for fill_deck to make the cards"""
        if value == 1:
            new_card = Card(suit, "A")
        elif value == 11:
            new_card = Card(suit, "J")
        elif value == 12:
            new_card = Card(suit, "Q")
        elif value == 13:
            new_card = Card(suit, "K")
        else:
            new_card = Card(suit, value)
        return new_card

    def shuffle_deck(self):
        """shuffles the deck"""
        random.shuffle(self.deck)

    def reset_deck(self):
        """resets the current deck"""
        self.deck.clear()
        self.__init__()

    def pop_card(self):
        """pops the top card from the deck"""
        return self.deck.pop(0)

    def __str__(self):
        """string representation of the deck"""
        deck_str = ", ".join(f"{card.__str__()}" for card in self.deck)
        return f"[{deck_str}]"
