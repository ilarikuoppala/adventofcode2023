from functools import reduce
with open('input.txt','r') as f:
 lines = f.readlines()

sum = 0
for line in lines:
    min_amount = {'red': 0, 'green': 0, 'blue': 0}
    game_id, cubes = line.strip().split(':')
    game_id = int(game_id.split()[1])
    games = cubes.split(';')
    for game in games:
       for color in game.split(','):
           count, color = color.split()
           min_amount[color] = max(min_amount[color], int(count))
    sum += reduce(lambda x,y: x*y, min_amount.values())
print(sum)
