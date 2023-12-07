import copy, pprint

with open('input.txt','r') as f:
    input = f.read().split('\n')

# Parsing and preprocessing
seed_ranges = list(map(int,input[0].split(':')[1].strip().split(' ')))
seeds = []
for i in range(len(seed_ranges)//2):
    seeds.append((seed_ranges[i*2], seed_ranges[i*2+1]))

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

# Fill in the empty slots
for map_type in map_list:
    current_map = maps[map_type]
    new_map = []
    current_map.sort(key = lambda x: x[1])
    map_max_value = current_map[-1][1] + current_map[-1][2]
    i=0
    j=0
    while i < map_max_value:
        if current_map[j][1] > i:
            new_map.append([i,i,current_map[j][1]-i])
        new_map.append(current_map[j])
        i = current_map[j][1] + current_map[j][2]
        j+=1
    maps[map_type] = new_map

# Recursive function to find out the final location
def traverse_maps(start, s_range, depth, solution):
    if depth == len(map_list):
        return min(start, solution)
    solutions = []
    for row in maps[map_list[depth]]:
        destination, source, range = row
        if start + s_range < source:
            continue
        elif start >= source+range:
            continue
        new_start = max(start, source)
        if start > source:
            destination += start-source
        new_end = min(start+s_range, source+range)
        new_range = new_end - new_start
        solutions.append(traverse_maps(destination, new_range, depth + 1, solution))
    if solutions:
        return min(solutions)
    return float('inf')

print(min([traverse_maps(seed, s_range, 0, float('inf')) for seed, s_range in seeds]))


