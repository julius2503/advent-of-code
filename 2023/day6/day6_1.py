def removeEmptyStrings(list):
    count = 0
    for value in list:
        if value == "":
            count+=1
    for i in range(count):
        list.remove('')
    return list

with open("./day6.txt", "r") as f:
    lines = f.readlines()
    time = lines[0]
    time = time.strip()
    time = time.split(" ")
    time = time[1:]
    time = removeEmptyStrings(time)
    distance = lines[1]
    distance = distance.split(" ")
    distance = distance[1:]
    distance = removeEmptyStrings(distance)
    print(time)
    print(distance)
    sum = 1
    for i in range(len(time)):
        winSum = 0
        cTime = int(time[i])
        cDistance = int(distance[i])
        count = 1
        while(count < cDistance):
            leftTime = cTime - count
            if leftTime * count > cDistance:
                winSum+=1
            count+=1
        sum*=winSum
    print(sum)
        
