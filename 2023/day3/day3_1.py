def findNumber(lines, i, j):
    string = ""
    # check left
    for x in range(j+1):
        if str(lines[i][j-x]).isdecimal():
            string += str(lines[i][j-x])
        else:
            break
    string = string[::-1]
    x = j+1
    while x < len(splitedLines[i]):
        if str(splitedLines[i][x]).isdecimal():
            string += splitedLines[i][x]
            x+=1
        else:
            break
    #print(string)
    return int(string)

def findDigits(lines, i, j):
    x = j
    count = 0
    while x < len(lines[i]):
        if str(lines[i][x]).isdecimal():
            count+=1
            x+=1
        else:
            break
    return count-1
     

notSymbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'} 
sum = 0
with open('2023/day3/day3.txt', 'r') as f:
    lines = f.read()
    lines = lines.splitlines()
    splitedLines = []
    for elem in lines:
        splitedLines.append(list(elem))
    for i, line in enumerate(lines):
        checksum = 0
        for j, letter in enumerate(line):
            if letter.isdecimal():
                # test if number already checked
                if checksum == 0:
                    # test the line above
                    if i > 0 and j > 0 and str(splitedLines[i-1][j-1]) not in notSymbols:
                        #print("case 1")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    elif i > 0 and str(splitedLines[i-1][j]) not in notSymbols:
                        #print("case 2")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    elif i > 0 and j < len(splitedLines[i])-1 and str(splitedLines[i-1][j+1]) not in notSymbols:
                        #print("case 3")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    # test same line
                    elif j > 0 and str(splitedLines[i][j-1]) not in notSymbols:
                        #print("case 4")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    elif j < len(splitedLines[1])-1 and str(splitedLines[i][j+1]) not in notSymbols:
                        #print("case 5")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    # test the line after
                    elif i < len(lines)-1 and j > 0 and str(splitedLines[i+1][j-1]) not in notSymbols:
                        #print("case 6")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    elif i < len(lines)-1 and str(splitedLines[i+1][j]) not in notSymbols:
                        #print("case 7")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                    elif i < len(lines)-1 and j < len(splitedLines[i])-1 and str(splitedLines[i+1][j+1]) not in notSymbols:
                        #print("case 8")
                        sum+=findNumber(splitedLines, i, j)
                        checksum += findDigits(splitedLines, i, j)
                else:
                    checksum-= 1
print(sum)

    

