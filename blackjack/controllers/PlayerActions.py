from models.Deck import Deck
from models.Player import Player
from models.Card import Card


def player_hit(deck, player):
    """remove a card from the deck and add it to the player's hand"""
    player.add_card_to_hand(deck.pop_card())


def player_stand():
    """TODO"""
    pass


def player_double_down():
    """TODO"""
    pass


def player_split():
    """TODO"""
    pass
