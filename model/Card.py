class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_card_value()

    def _get_card_value(self):
        """Assign values to cards based on Blackjack rules."""
        if self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # In Blackjack, Aces can be 1 or 11; initial value is 11

    def __str__(self):
        """String representation of the card."""
        return f"{self.rank} of {self.suit}"

# Example usage:
if __name__ == "__main__":
    # Create a sample card
    sample_card = Card(suit="Hearts", rank="8")

    # Print the card details
    print("Card:", sample_card)
    print("Suit:", sample_card.suit)
    print("Rank:", sample_card.rank)
    print("Value:", sample_card.value)
