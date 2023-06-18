import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card_1 = Card("Spades", 1)
        self.card_2 = Card("Diamonds", 2)
        self.card_3 = Card("Clubs", 3)
        self.card_4 = Card("Hearts", 4)
   
    def test_check_for_ace__pass(self):
        result = self.card_game.check_for_ace(self.card_1)
        self.assertEqual(True, result)

    def test_check_for_ace__fail(self):
        result = self.card_game.check_for_ace(self.card_3)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card_2, self.card_4)
        self.assertEqual(4, result.value)

    def test_cards_total(self):
        cards = [self.card_1, self.card_2, self.card_3, self.card_4]
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 10", result)