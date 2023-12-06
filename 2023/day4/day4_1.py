def removeEmptyStrings(list):
    count = 0
    for value in list:
        if value == "":
            count+=1
    for i in range(count):
        list.remove('')
    return list

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
        ownCards
        print(winningCards)
        print(ownCards)
        
        for wCard in winningCards:
            if wCard in ownCards:
                if lineSum == 0:
                    lineSum = 1
                else:
                    lineSum*=2
        sum+=lineSum

print(sum)
        
