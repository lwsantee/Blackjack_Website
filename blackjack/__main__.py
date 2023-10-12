from .models.Card import Card
from .models.Player import Player

# Create a sample player
player1 = Player(name="Alice")

# Add cards to the player's hand
card1 = Card(suit="Hearts", rank="8")
card2 = Card(suit="Diamonds", rank="K")

player1.add_card_to_hand(card1)
player1.add_card_to_hand(card2)

# Print player details and hand value
print(player1)
print("Hand:", [str(card) for card in player1.hand])
print("Total Hand Value:", player1.calculate_hand_value())
