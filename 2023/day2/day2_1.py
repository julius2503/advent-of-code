def check(y):
    if "red" in y:
        value = y.split(" ")
        if int(value[1]) > 12:
            return False
    elif "green" in y:
        value = y.split(" ")
        if int(value[1]) > 13:
            return False
    elif "blue" in y:
        value = y.split(" ")
        if int(value[1]) > 14:
            return False

def isPossible(word):
    for i in word:
            for j in i:
                if check(j) == False:
                    return False
    return True

sum = 0
with open('./day2.txt', 'r') as f:
    for line in f.readlines():
        x = line.split(":") # ['Game 4', ' 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n']
        game = x[0] # Game 5
        game = game.split(" ") # ['Game', '5']
        gameValue = game[1] # 5
        sum+=int(gameValue)
        picks = x[1] # 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        combination = picks.split(";") # [' 6 red, 1 blue, 3 green', ' 2 blue, 1 red, 2 green']
        word = []
        for pick in combination:
            word.append(pick.split(",")) # [[' 6 red', ' 1 blue', ' 3 green'], [' 2 blue', ' 1 red', ' 2 green']]
        if isPossible(word) == False:
            sum-= int(gameValue)

    print(sum)    
    
