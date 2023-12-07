with open('input.txt','r') as f:
    lines = f.readlines()

races = []
time = int(lines[0].split(':')[1].replace(' ','').strip())
distance = int(lines[1].split(':')[1].replace(' ','').strip())

for race in range(1):
    ways_to_win = 0
    for i in range(time):
        ways_to_win += (1 if i * (time-i) > distance else 0)
print(ways_to_win)
