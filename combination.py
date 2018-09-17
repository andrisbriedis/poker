from collections import Counter

CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Combination(object):

    def apply(self, cards):
        raise NotImplementedError()

    def compare(self,other) -> str:
        raise NotImplementedError()

class NoneCombination(Combination):
    def apply(self, cards):
        return self

    def find_max(self,cards):
        self_values = [CARD_VALUES.index(value[0]) for value in cards]
        return max(self_values)

    def compare(self,other) -> str:
        self_max = self.find_max()

class Pair(Combination):
    def apply(self, cards):
        pair_card, count = self.find_most_common(cards)

        if count == 2:
            self.pair_card = pair_card
            return self
        else:
            return None

    def find_most_common(self, cards):
        self_values = [CARD_VALUES.index(value[0]) for value in cards]
        result = Counter(self_values)
        return result.most_common(1)[0]


COMBINATIONS = [Pair, NoneCombination]
