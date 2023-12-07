from collections import Counter

with open('input.txt','r') as f:
    input = f.read().strip().split('\n')

def get_hand_type(hand):
    cards = sorted(list(hand))
    different_cards = len(set(cards))
    c = Counter(cards)
    if 'J' in c:
        c.pop("J")
        jokers = 5 - sum(c.values())
        if len(c) == 1:
            return 6
        if jokers > 3:  # 5 of a kind
            return 6
        if jokers == 3:
            return (6 if 2 in c.values() else 5)
        if jokers == 2:
            if len(c) == 2:
                return 5
            return 3
        if 3 in c.values():
            return 5
        if len(c) == 3:
            return 3
        if len(c) == 2 and 2 in c.values():
            return 4
        return 1
    if 5 in c.values():
        return 6  # five
    elif 4 in c.values():
        return 5  # four
    elif 3 in c.values() and 2 in c.values():
        return 4  # full house
    elif 3 in c.values():
        return 3  # three of a kind
    elif 2 in c.values() and len(set(cards)) == 3:
        return 2  # two pair
    elif 2 in c.values():
        return 1  # pair
    else:
        return 0  # high


def get_hand_value(hand):
    translation = {'2': 'a', '3': 'b', '4': 'c', '5': 'd', '6':'e', '7':'f', '8': 'g', '9': 'h', 'T': 'i', 'J': 'A', 'Q': 'k', 'K': 'l', 'A':'m'}
    value_str = ""
    for card in hand:
        value_str += translation[card]
    return value_str

hands_by_type = [list() for x in range(7)]

for row in input:
    hand, bet = row.split()
    hand_type = get_hand_type(hand)
    hand_value = get_hand_value(hand)
    hands_by_type[hand_type].append((hand_value, hand, bet))

all_hands = []
for hand_type in hands_by_type:
    hand_type.sort(key = lambda x: x[0])
    all_hands += hand_type

sum = 0
for i in range(len(input)):
    sum += (i+1) * int(all_hands[i][2])

print(sum)
