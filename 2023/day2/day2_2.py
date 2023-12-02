def check(word):
    allSum = 0
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for i in word:
        for j in i:
            value = j.split(" ")
            value[2] = value[2].replace("\n", "")
            if value[2] == "red":
                if int(value[1]) > maxRed:
                    maxRed = int(value[1])
            elif value[2] == "blue":
                if int(value[1]) > maxBlue:
                    maxBlue = int(value[1])
            elif value[2] == "green":
                if int(value[1]) > maxGreen:
                    maxGreen = int(value[1])
    #print(str(maxBlue) + " " + str(maxGreen) + " " + str(maxRed))
    allSum = maxGreen * maxBlue * maxRed
    return allSum



sum = 0
with open('2023/day2/day2.txt', 'r') as f:
    for line in f.readlines():
        x = line.split(":") # ['Game 4', ' 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n']
        picks = x[1] # 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        combination = picks.split(";") # [' 6 red, 1 blue, 3 green', ' 2 blue, 1 red, 2 green']
        word = []
        for pick in combination:
            word.append(pick.split(",")) # [[' 6 red', ' 1 blue', ' 3 green'], [' 2 blue', ' 1 red', ' 2 green']]
        lineSum = int(check(word))
        sum = sum + lineSum
print(sum)