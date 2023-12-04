def findValue(i, j):
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

def findDigit(i, j, w, x, y, z):
    # test the line before
    if  (i > 0 and j > 0 and 
        str(splitedLines[i-1][j-1]) in digits and 
        w != i-1 and x != j-1 and y != i-1 and z != j-1
        ):
            return i-1, j-1, findValue(i-1, j-1)
    
    elif(i > 0 and 
        str(splitedLines[i-1][j]) in digits and 
        w != i-1 and x != j and y != i-1 and z != j
        ):
            return i-1, j, findValue(i-1, j)
    
    elif(i > 0 and j < len(splitedLines[i])-1 and
        str(splitedLines[i-1][j+1]) in digits and 
        w != i-1 and x != j+1 and y != i-1 and z != j+1
        ):
            return i-1, j+1, findValue(i-1, j+1)
    
    # test same line
    elif(j > 0 and 
        str(splitedLines[i][j-1]) in digits and 
        w != i and x != j-1 and y != i and z != j-1
        ):
            return i, j-1, findValue(i, j-1)
    
    elif(j < len(splitedLines[1])-1 and 
        str(splitedLines[i][j+1]) in digits and 
        w != i and x != j+1 and y != i and z != j+1
        ):
            return i, j+1, findValue(i, j+1)

    # test the line after
    elif(i < len(lines)-1 and j > 0 and 
         str(splitedLines[i+1][j-1]) in digits and 
         w != i+1 and x != j-1 and y != i+1 and z != j-1
         ):
            return i+1, j-1, findValue(i+1, j-1)

    elif(i < len(lines)-1 and 
        str(splitedLines[i+1][j]) in digits and 
        w != i+1 and x != j and y != i+1 and z != j
        ):
            return i+1, j, findValue(i+1, j)
    
    elif(i < len(lines)-1 and j < len(splitedLines[i])-1 and 
        str(splitedLines[i+1][j+1]) in digits and 
        w != i+1 and x != j+1 and y != i+1 and z != j+1
        ):
            return i+1, j+1, findValue(i+1, j+1)
    else:
        return -1, -1, -1

digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} 
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
            if letter == "*":
                res1 = findDigit(i, j, -1, -1, -1, -1)
                if res1[0] != -1:
                    w = res1[0]
                    x = res1[1]
                    value1 = res1[2]
                    res2 = findDigit(i, j, w, x, -1, -1)
                    if res2[0] != -1:
                        y = res2[0]
                        z = res2[1]
                        value2 = res2[2]
                        res3 = findDigit(i, j, w, x, y, z)
                        if res3[0] == -1:
                            value = value1 * value2
                            sum += value

print(sum)

    

