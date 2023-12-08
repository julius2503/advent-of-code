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
    cTime = ""
    cDistance = ""
    for value in time:
        cTime = cTime + value
    for value in distance:
        cDistance = cDistance + value
    cTime = int(cTime)
    cDistance = int(cDistance)
    count = 1
    sum = 0
    while(sum == 0):
        leftTime = cTime - count
        if leftTime * count > cDistance:
            sum+=1
            break
        count+=1
    print(count)
    count2 = cTime
    while(sum != 0):
        leftTime = cTime - count2
        if leftTime * count2 > cDistance:
            sum-=1
            break
        count2-=1
    print(count2)
print(count2 - count + 1)