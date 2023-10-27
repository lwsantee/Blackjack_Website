from typing import Dict, List, Self
from blackjack.models.Card import Card


class Player:

    active_players: Dict[str, Self] = {}

    def __init__(self, name: str, balance: float, seat: int):
        self.name = name
        self.hand = []
        self.balance = balance
        self.bet = 0
        self.seat = seat

    def add_card_to_hand(self, card):
        """add a card to the player's hand"""
        self.hand.append(card)

    def calculate_hand_value(self):
        """calculate the total value of the player's hand"""
        hand_value = sum(card.value for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')
        # adjust for aces if the total value is greater than 21
        while num_aces > 0 and hand_value > 21:
            # convert ace from 11 to 1
            hand_value -= 10
            num_aces -= 1
        return hand_value

    def make_bet(self, bet_amount):
        """makes a bet using the player's money"""
        # if the player cannot bet that amount, return false
        if bet_amount > self.balance:
            return False
        # otherwise, make the bet and return true
        else:
            self.balance -= bet_amount
            self.bet += bet_amount
            return True

    def check_for_split(self):
        """TODO"""
        pass

    def player_has_blackjack(self):
        """checks if the player has hit blackjack"""
        if self.calculate_hand_value() == 21 and self.hand.__len__() == 2:
            return True
        else:
            return False

    def has_player_bust(self):
        """checks if the player has gone over 21"""
        if self.calculate_hand_value() > 21:
            return True
        else:
            return False

    def clear_hand(self):
        """clear the player's hand"""
        self.hand = []

    def clear_bet(self):
        """clear the player's bet"""
        self.bet = 0

    def __str__(self):
        """string representation of the player"""
        hand_str = ", ".join(
            f"{card.__str__()}" for card in self.hand)
        return f"{self.name} (Balance: ${self.balance}, Hand: [{hand_str}])"
