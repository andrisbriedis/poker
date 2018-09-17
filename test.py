import unittest
from hand import Hand


class PokerHandTest(unittest.TestCase):
    def test_high_card_wins(self):
        handOne = Hand("KS 2H 5C JD TD")
        handTwo = Hand("3S 4C 9D QC 6H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("Win", result)

    def test_high_pair_wins(self):
        handOne = Hand("KS KH 5C JD TD")
        handTwo = Hand("4S 3C 9D AC 6H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("Win", result)

    def test_high_card_pair_wins(self):
        handOne = Hand("KS KH 5C JD TD")
        handTwo = Hand("KD KC 9D AC 6H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("Loss", result)

    def test_highest_pair_wins(self):
        handOne = Hand("KS KH 5C JD TD")
        handTwo = Hand("2D 2C 9D AC 6H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("Win", result)

    def test_three_of_a_kind_wins_pair(self):
        handOne = Hand("KS KH 5C JD TD")
        handTwo = Hand("2D 2C 2H AC 6H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("Loss", result)