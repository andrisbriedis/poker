from collections import Counter
from typing import Optional

from combination import COMBINATIONS, Combination, NoneCombination


class Hand(object):
    CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, hand: str):
        self.__hand = hand.split(" ")

    def get_cards(self):
        return list(self.__hand)

    def find_combination(self):
        for combination_type in COMBINATIONS:
            combination = combination_type().apply(self.__hand)
            if combination:
                return combination

    def rank(self, combination: Optional[Combination]) -> int:
        return COMBINATIONS.index(combination.__class__)

    def compare_with(self, other):
        self_combination = self.find_combination()
        other_combination = other.find_combination()

        if self.rank(self_combination) < self.rank(other_combination):
            return "Win"
        elif self.rank(self_combination) > self.rank(other_combination):
            return "Loss"

        result = self_combination.compare(other_combination)
        if result == 'Tie':
            self_combination = NoneCombination().apply(self.get_cards())
            other_combination = NoneCombination().apply(other.get_cards())
            result = self_combination.compare(other_combination)

        return result

    def has_pair(self):
        most_common = self.find_pair()
        most_common_count = most_common[1]
        return most_common_count == 2

    def find_pair(self):
        self_values = [self.CARD_VALUES.index(value[0]) for value in self.__hand]
        result = Counter(self_values)
        return result.most_common(1)[0]
