sum = 0
with open('2023/day4/day4.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        lineSum = 0
        cards = line.split(":")[1]
        winningCards = cards.split("|")[0].split(" ")
        ownCards = cards.split("|")[1].split(" ")
        for card in winningCards:
            if card == '':
                winningCards.remove('')
        for card in ownCards:
            if card == '':
                ownCards.remove('')
            ownCards[-1] = ownCards[-1].replace("\n", "")
        print(winningCards)
        print(ownCards)
        print("")
        
        for wCard in winningCards:
            if wCard in ownCards:
                if lineSum == 0:
                    lineSum = 1
                else:
                    lineSum*=2
        sum+=lineSum

print(sum)
        
