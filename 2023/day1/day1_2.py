sum = 0
with open('./day1.txt', 'r') as f:
    for line in f.readlines():
        lineSum = ""
        for i in range(len(line)):
            if line[i].isnumeric() == True:
                lineSum = str(line[i])
                print(line[i])
                break
            elif line[i] == 'o' and line[i+1] == "n" and line[i+2] == 'e':
                lineSum = str(1)
                print(1)
                break
            elif line[i] == 't' and line[i+1] == "w" and line[i+2] == 'o':
                lineSum = str(2)
                print(2)
                break
            elif line[i] == 't' and line[i+1] == "h" and line[i+2] == 'r' and line[i+3] == 'e' and line[i+4] == 'e':
                lineSum = str(3)
                print(3)
                break
            elif line[i] == 'f' and line[i+1] == "o" and line[i+2] == 'u' and line[i+3] == 'r':
                lineSum = str(4)
                print(4)
                break
            elif line[i] == 'f' and line[i+1] == "i" and line[i+2] == 'v' and line[i+3] == 'e':
                lineSum = str(5)
                print(5)
                break
            elif line[i] == 's' and line[i+1] == "i" and line[i+2] == 'x':
                lineSum = str(6)
                print(6)
                break
            elif line[i] == 's' and line[i+1] == "e" and line[i+2] == 'v' and line[i+3] == 'e' and line[i+4] == 'n':
                lineSum = str(7)
                print(7)
                break
            elif line[i] == 'e' and line[i+1] == "i" and line[i+2] == 'g' and line[i+3] == 'h' and line[i+4] == 't':
                lineSum = str(8)
                print(8)
                break
            elif line[i] == 'n' and line[i+1] == "i" and line[i+2] == 'n' and line[i+3] == 'e':
                lineSum = str(9)
                print(9)
                break

        for i in range(len(line)):
            i = i + 1
            if line[-i].isnumeric() == True:
                lineSum += str(line[-i])
                print(line[-i])
                break
            elif line[-i] == 'e' and line[-(i+1)] == "n" and line[-(i+2)] == 'o':
                lineSum += str(1)
                print(1)
                break
            elif line[-i] == 'o' and line[-(i+1)] == "w" and line[-(i+2)] == 't':
                lineSum += str(2)
                print(2)
                break
            elif line[-i] == 'e' and line[-(i+1)] == "e" and line[-(i+2)] == 'r' and line[-(i+3)] == 'h' and line[-(i+4)] == 't':
                lineSum += str(3)
                print(3)
                break
            elif line[-i] == 'r' and line[-(i+1)] == "u" and line[-(i+2)] == 'o' and line[-(i+3)] == 'f':
                lineSum += str(4)
                print(4)
                break
            elif line[-i] == 'e' and line[-(i+1)] == "v" and line[-(i+2)] == 'i' and line[-(i+3)] == 'f':
                lineSum += str(5)
                print(5)
                break
            elif line[-i] == 'x' and line[-(i+1)] == "i" and line[-(i+2)] == 's':
                lineSum += str(6)
                print(6)
                break
            elif line[-i] == 'n' and line[-(i+1)] == "e" and line[-(i+2)] == 'v' and line[-(i+3)] == 'e' and line[-(i+4)] == 's':
                lineSum += str(7)
                print(7)
                break
            elif line[-i] == 't' and line[-(i+1)] == "h" and line[-(i+2)] == 'g' and line[-(i+3)] == 'i' and line[-(i+4)] == 'e':
                lineSum += str(8)
                print(8)
                break
            elif line[-i] == 'e' and line[-(i+1)] == "n" and line[-(i+2)] == 'i' and line[-(i+3)] == 'n':
                lineSum += str(9)
                print(9)
                break
        sum += int(lineSum)
print(sum)