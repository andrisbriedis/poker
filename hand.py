from collections import Counter

class Hand:
    CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, hand: str):
      self.__hand = hand.split(" ")

    def compare_with(self, other):

        self_max = self.find_max()
        other_max = other.find_max()

        if self.has_pair() or other.has_pair():
            if self.has_pair() and not other.has_pair():
                return "Win"
            if not self.has_pair() and other.has_pair():
                return "Loss"
            self_value, _ = self.find_pair()
            other_value, _ = other.find_pair()
            if self_value != other_value:
                if self_value > other_value:
                    return "Win"
                elif self_value < other_value:
                    return "Loss"

        if self_max > other_max:
          return "Win"
        elif self_max < other_max:
          return "Loss"
        else:
          return "Tie"

    def find_max(self):
        self_values = [self.CARD_VALUES.index(value[0]) for value in self.__hand]
        return max(self_values)

    def has_pair(self):
        most_common = self.find_pair()
        most_common_count = most_common[1]
        return most_common_count == 2

    def find_pair(self):
        self_values = [self.CARD_VALUES.index(value[0]) for value in self.__hand]
        result = Counter(self_values)
        return result.most_common(1)[0]
