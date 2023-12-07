from collections import Counter

with open('input.txt','r') as f:
    input = f.read().strip().split('\n')

def get_hand_type(hand):
    cards = sorted(list(hand))
    different_cards = len(set(cards))
    c = Counter(cards)
    if 5 in c.values():
         return 6
    elif 4 in c.values():
        return 5
    elif 3 in c.values() and 2 in c.values():
        return 4
    elif 3 in c.values():
        return 3
    elif 2 in c.values() and len(set(cards)) == 3:
        return 2
    elif 2 in c.values():
        return 1
    else:
        return 0


def get_hand_value(hand):
    translation = {'2': 'a', '3': 'b', '4': 'c', '5': 'd', '6':'e', '7':'f', '8': 'g', '9': 'h', 'T': 'i', 'J': 'j', 'Q': 'k', 'K': 'l', 'A':'m'}
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
