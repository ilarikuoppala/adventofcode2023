with open('input.txt','r') as f:
    sum = 0
    for line in f.readlines():
        first = ""
        last = ""
        for char in line:
            if char.isnumeric():
                if first == "":
                    first = char
                last = char
        print(first+last)
        sum += int(first+last)
print(sum)
