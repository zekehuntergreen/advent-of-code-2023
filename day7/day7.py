from functools import total_ordering

PART_2 = True


@total_ordering
class Card:
    face_card_values = {"A": 14, "K": 13, "Q": 12, "J": 1 if PART_2 else 11, "T": 10}

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.__get_card_score(self.value) < self.__get_card_score(other.value)

    def __get_card_score(self, value):
        if value in self.face_card_values:
            value = self.face_card_values[value]
        return int(value)


@total_ordering
class Hand:
    hand_type_values = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5],
    ]

    def __init__(self, hand, wager):
        self.hand = [Card(c) for c in hand]
        self.wager = wager
        self.type_score = (
            self.__get_type_score_part_2(hand)
            if PART_2
            else self.__get_type_score_part_1(hand)
        )

    def __lt__(self, other):
        if self.type_score != other.type_score:
            return self.type_score < other.type_score
        for i, this_card in enumerate(self.hand):
            if this_card != other.hand[i]:
                return this_card < other.hand[i]

    def __get_type_score(self, hand):
        hand_dict = {}
        for c in hand:
            if c in hand_dict:
                hand_dict[c] += 1
            else:
                hand_dict[c] = 1
        return sorted(hand_dict.values(), reverse=-1)

    def __get_type_score_part_2(self, hand):
        num_jokers = len([c for c in hand if c == "J"])
        hand_without_jokers = hand.replace("J", "")
        hand_values = self.__get_type_score(hand_without_jokers)
        if not hand_values:  # handles "JJJJJ"
            hand_values = [0]
        hand_values[0] += num_jokers
        return self.hand_type_values.index(hand_values)

    def __get_type_score_part_1(self, hand):
        hand_values = self.__get_type_score(hand)
        return self.hand_type_values.index(hand_values)


hands = []
for line in open("input/puzzle_input.txt").readlines():
    hand_string, wager = line.split()
    hands.append(Hand(hand_string, int(wager)))

print(sum([h.wager * (i + 1) for i, h in enumerate(sorted(hands))]))
