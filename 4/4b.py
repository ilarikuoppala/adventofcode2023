with open('input.txt','r') as f:
 cards = f.read().split('\n')[:-1]


wins = [0] * len(cards)
copies = [1] * len(cards)

i = 0
for card in cards:
    i += 1  # card numbering starts from 1
    winning_numbers, my_numbers = card.split(':')[1].split('|')
    winning = list(map(int, winning_numbers.split()))
    my = list(map(int, my_numbers.split()))
    count = 0
    for number in my:
        if number in winning:
            count += 1
    wins[i-1] = count

for i in range(len(copies)):
    win = wins[i]
    for j in range(i+1, min(i+win+1, len(cards))):
        copies[j] += 1 * copies[i]
print(sum(copies))
