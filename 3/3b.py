with open('input.txt', 'r') as f:
   rows = f.readlines()
sum = 0
potential_gear_numbers = {}

def count_numbers(grid):
    numbers = 0
    number_positions = []
    for i in range(len(grid)):
        text = grid[i]
        row_numbers = 0
        if text[0].isnumeric():
            row_numbers = 1
            number_positions.append((0,i))
            if len(text) == 3 and not text[1].isnumeric() and text[2].isnumeric():
                number_positions.append((2,i))
                row_numbers = 2
        elif text[1].isnumeric():
            number_positions.append((1,i))
            row_numbers = 1
        elif text[2].isnumeric():
            number_positions.append((2,i))
            row_numbers = 1
        numbers += row_numbers
    return numbers, number_positions

def get_number(x,y,position):
    column = x + position[0] - 1
    row = rows[y + position[1] -1]
    number_str = row[column]
    i = 1
    while row[column+i].isnumeric():
        number_str += row[column+i]
        i+=1
    i = 1
    while row[column-i].isnumeric():
        number_str = row[column-i] + number_str
        i+=1
    return int(number_str)

def is_gear(x,y):
    adjacent_rows = rows[max(0,y-1):y+2]
    grid = []
    if y == 0:
        grid.append('...')
    for row in adjacent_rows:
        grid.append(row[max(0,x-1):x+2])
    if len(grid) == 2:
        grid.append('...')
    part_count = 0
    number_count, positions = count_numbers(grid)
    if number_count == 2:
        # I'm assuming here that the part number isn't zero
        return get_number(x,y,positions[0])*get_number(x,y,positions[1])

is_gear(10,10)
sum = 0
for i in range(len(rows)):
    row = rows[i]
    for j in range(len(row)):
        if row[j] == "*" and is_gear(j,i):
            sum += is_gear(j,i)
print(sum)
