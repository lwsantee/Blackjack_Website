class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        """Add a card to the player's hand."""
        self.hand.append(card)

    def calculate_hand_value(self):
        """Calculate the total value of the player's hand."""
        hand_value = sum(card.value for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')

        # Adjust for Aces if the total value is greater than 21
        while num_aces > 0 and hand_value > 21:
            hand_value -= 10  # Convert Ace from 11 to 1
            num_aces -= 1

        return hand_value

    def clear_hand(self):
        """Clear the player's hand."""
        self.hand = []

    def __str__(self):
        """String representation of the player."""
        return f"Player {self.name}"
