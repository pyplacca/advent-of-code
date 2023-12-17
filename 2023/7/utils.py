from typing import Literal, Iterable


CardType = Literal[
    "five_of_a_kind",
    "four_of_a_kind",
    "full_house",
    "three_of_a_kind",
    "two_pair",
    "one_pair",
    "high_card",
]
CardLabel = Literal[
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]


class CamelCardBase:
    label_strength: dict[CardLabel, int] = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }
    type_strength: dict[CardType, int] = {
        "five_of_a_kind": 7,
        "four_of_a_kind": 6,
        "full_house": 5,
        "three_of_a_kind": 4,
        "two_pair": 3,
        "one_pair": 2,
        "high_card": 1,
    }

    def __init__(self, hand: str):
        self.hand = hand
        self.total_labels = len(hand)
        self.total_unique_labels = len(set(hand))

    def __str__(self):
        return self.hand

    def __lt__(self, other):
        return self.compare(self, other) == "<"

    def __gt__(self, other):
        return self.compare(self, other) == ">"

    def __eq__(self, other):
        return self.compare(self, other) == "=="

    @staticmethod
    def compare(this, other) -> Literal["<", "==", ">"]:
        if not this.strength == other.strength:
            return ">" if this.strength > other.strength else "<"

        comparator = "=="
        index = 0

        while index < this.total_labels:
            a, b = map(
                lambda label: this.label_strength[label],
                [this.hand[index], other.hand[index]],
            )
            if a == b:
                index += 1
                continue

            comparator = ">" if a > b else "<"
            break

        return comparator

    @property
    def label_counts(self) -> dict[CardLabel, int]:
        hash = {}
        for label in self.hand:
            hash[label] = hash.get(label, 0) + 1
        return hash

    @property
    def type(self) -> CardType:
        counts = list(self.label_counts.values())
        value: CardType = "high_card"

        if self.total_unique_labels == 1:
            value = "five_of_a_kind"

        elif self.total_unique_labels == 2:
            value = "four_of_a_kind"

            if 2 in counts:
                value = "full_house"

        elif self.total_unique_labels == 3:
            value = "three_of_a_kind"

            if counts.count(2) == 2:
                value = "two_pair"

        elif counts.count(2) == 1:
            value = "one_pair"

        return value

    @property
    def strength(self):
        return self.type_strength[self.type]


class CamelCard(CamelCardBase):
    """Eg: CamelCard('AA8AA')"""

    def __repr__(self):
        return f"CamelCard<hand='{self.hand}', type='{self.type}', strength={self.strength}>"

    @staticmethod
    def strongest(*cards: Iterable[CamelCardBase]) -> CamelCardBase:
        result = cards[0]
        for card in cards[1:]:
            if card > result:
                result = card
        return result

    @staticmethod
    def weakest(*cards: Iterable[CamelCardBase]) -> CamelCardBase:
        result = cards[0]
        for card in cards[1:]:
            if card < result:
                result = card
        return result
