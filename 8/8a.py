with open('input.txt','r') as f:
    input = f.read().strip().split('\n')

instructions = input[0]

network = {}

for item in input[2:]:
    location, neighbours = item.split(' = ')
    network[location] = neighbours.strip('()').split(', ')

key = {"L": 0, "R": 1}
position = "AAA"
i = 0
while position != "ZZZ":
    position = network[position][key[instructions[i%len(instructions)]]]
    i+=1
print(i)

