def removeEmptyStrings(list):
    count = 0
    for value in list:
        if value == "":
            count+=1
    for i in range(count):
        list.remove('')
    return list

winningList = []
sum = 0
with open('./day4.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        lineSum = 0
        line = line.strip()
        cards = line.split(":")[1]
        winningCards = cards.split("|")[0].split(" ")
        ownCards = cards.split("|")[1].split(" ")
        winningCards = removeEmptyStrings(winningCards)
        ownCards = removeEmptyStrings(ownCards)
        
        for wCard in winningCards:
            if wCard in ownCards:
                lineSum+=1
        winningList.append(lineSum)

instances = [1 for x in winningList]
winningList = [int(x) for x in winningList]
for i, card in enumerate(winningList):
    for j in range(card):
        if i+j+1 < len(winningList):
            instances[i+j+1]+= instances[i]
for value in instances:
    sum += value
print(sum)
 
