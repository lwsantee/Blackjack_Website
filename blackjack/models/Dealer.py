class Player:

    def __init__(self):
        self.hand = []

    def add_card_to_hand(self, card):
        """Add a card to the dealer's hand"""
        self.hand.append(card)

    def calculate_hand_value(self):
        """Calculate the total value of the dealer's hand"""
        hand_value = sum(card.value for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')

        # Adjust for Aces if the total value is greater than 21
        while num_aces > 0 and hand_value > 21:
            # Convert Ace from 11 to 1
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def clear_hand(self):
        """Clear the dealers's hand"""
        self.hand = []
