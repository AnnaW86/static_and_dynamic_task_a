import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('hearts', 5)
        self.card3 = Card('clubs', 10)
        self.card4 = Card('spades', 8)
        self.card5 = Card('diamonds', 12)
        self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
        self.game = CardGame()
    
    def test_check_for_ace(self):
        result = self.game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_check_for_not_ace(self):
        result = self.game.check_for_ace(self.card2)
        self.assertEqual(False, result)
    
    def test_highest_card(self):
        result = self.game.highest_card(self.card3, self.card4)
        self.assertEqual(self.card3, result)
    
    def test_cards_total(self):
        result = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 36", result)

