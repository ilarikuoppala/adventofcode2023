with open('input.txt','r') as f:
    input = f.read().split('\n')

# Parsing and preprocessing
seeds = list(map(int,input[0].split(':')[1].strip().split(' ')))

map_list = []
maps = {}
current_map = ''
for line in input:
    if 'map' in line:
        current_map = line.split(' ')[0]
        map_list.append(current_map)
        maps[current_map] = []
    elif line and current_map:
        maps[current_map].append(list(map(int, line.split())))

# Recursive function to find out the final location
def traverse_maps(position, depth):
    if depth == len(map_list):
        return position
    for row in maps[map_list[depth]]:
        destination, source, range = row
        if position >= source and source+range > position:
            return traverse_maps(destination + (position - source), depth + 1)
    return float('inf')  # inf instead of None to find the nearest location

print(min([traverse_maps(seed, 0) for seed in seeds]))

