sum = 0
with open('2023/day1/day1.txt', 'r') as f:
    for line in f.readlines():
        lineSum = ""
        for letter in line:
            if letter.isnumeric() == True:
                lineSum = str(letter)
                print(letter)
                break
        for letter in reversed(line):
            if letter.isnumeric() == True:
                lineSum = lineSum + str(letter)
                print(letter)
                break
        sum += int(lineSum)
print(sum)
        