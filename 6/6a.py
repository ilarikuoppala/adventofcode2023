with open('input.txt','r') as f:
    lines = f.readlines()

races = []
i = 0
times = list(map(int,lines[0].split(':')[1].split()))
distances = list(map(int,lines[1].split(':')[1].split()))

answer = 1
for race in range(len(times)):
    ways_to_win = 0
    time = times[race]
    distance = distances[race]
    for i in range(time):
        ways_to_win += (1 if i * (time-i) > distance else 0)
    answer *= ways_to_win
print(answer)
