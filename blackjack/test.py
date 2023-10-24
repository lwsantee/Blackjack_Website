from models.Deck import Deck
from models.Player import Player
from controllers.PlayerActions import *

deck = Deck()
print(deck.__str__())
logan = Player("Logan", 100)
player_hit(deck, logan)
player_hit(deck, logan)
print(logan.__str__())
print(deck.__str__())
