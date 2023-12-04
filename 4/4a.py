with open('input.txt','r') as f:
 cards = f.read().split('\n')[:-1]


sum = 0
for card in cards:
    winning_numbers, my_numbers = card.split(':')[1].split('|')
    winning = list(map(int, winning_numbers.split()))
    my = list(map(int, my_numbers.split()))
    count = 0
    for number in my:
        if number in winning:
            count += 1
    if count:
        sum += 2**(count-1)
print(sum)
