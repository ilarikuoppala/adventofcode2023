
with open('input.txt','r') as f:
 lines = f.readlines()

requirements = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
for line in lines:
    game_id, cubes = line.strip().split(':')
    game_id = int(game_id.split()[1])
    games = cubes.split(';')
    possible = 1
    for game in games:
       for color in game.split(','):
           count, color = color.split()
           if requirements[color] < int(count):
               possible = 0
    if possible:
       sum += game_id
print(sum)
