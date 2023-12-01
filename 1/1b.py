def find_digits(input):
    digit_positions = {}
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 0
    for char in input:
        if char.isnumeric():
            digit_positions[i] = int(char)
        else:
            for digit in digits:
                if input[i:].startswith(digit):
                    digit_positions[i] = digits.index(digit) + 1
        i+=1
    first = min(digit_positions.keys())
    last = max(digit_positions.keys())
    return int(str(digit_positions[first])+str(digit_positions[last]))

with open('input.txt','r') as f:
    sum = 0
    for line in f.readlines():
        sum += find_digits(line)
print(sum)
