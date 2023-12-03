with open('input.txt', 'r') as f:
   rows = f.readlines()
sum = 0
for i in range(0,len(rows)):
    adjacent_rows = rows[max(0,i-1):i+2]
    row = rows[i]
    j = 0
    while j < len(row):
        if row[j].isnumeric():
            number_str = ""
            k = 0
            while row[j+k].isnumeric():
                number_str += row[j+k]
                k+=1
            number = int(number_str)
            for adjacent in adjacent_rows:
                if not adjacent[max(0,j-1):j+k+1].rstrip().replace('.','a').isalnum():
                    sum += number
                    print("Part",number)
                    for a in adjacent_rows:
                        print(a[max(0,j-1):j+k+1].replace('.','.'))
                    break
            j += len(number_str)
        else:
            j+=1
print(sum)
