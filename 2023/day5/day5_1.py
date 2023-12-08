with open("./day5.txt", "r") as f:
    content = f.read()
    content = content.split("\n\n")
    seeds = content[0]
    soil = content[1]
    fertilizer = content[2]
    water = content[3]
    light = content[4]
    temperature = content[5]
    humidity = content[6]
    location = content[7]

## split seeds
seeds = seeds.split(" ")
seeds = seeds[1:]
seeds = [int(x) for x in seeds]
newSeeds = []
for i, seed in enumerate(seeds):
    if i % 2 == 0:
        for j in range(seeds[i + 1]):
            print(seed+j)
            newSeeds.append(seed+j)
print(newSeeds)

## split soil
soil = soil.split("\n")
soil = soil[1:]
for i, j in enumerate(soil):
    soil[i] = j.split(" ")
    soil[i] = [int(x) for x in soil[i]]

## split fertilizer
fertilizer = fertilizer.split("\n")
fertilizer = fertilizer[1:]
for i, j in enumerate(fertilizer):
    fertilizer[i] = j.split(" ")
    fertilizer[i] = [int(x) for x in fertilizer[i]]

## split water
water = water.split("\n")
water = water[1:]
for i, j in enumerate(water):
    water[i] = j.split(" ")
    water[i] = [int(x) for x in water[i]]

## split light
light = light.split("\n")
light = light[1:]
for i, j in enumerate(light):
    light[i] = j.split(" ")
    light[i] = [int(x) for x in light[i]]

## split temperature
temperature = temperature.split("\n")
temperature = temperature[1:]
for i, j in enumerate(temperature):
    temperature[i] = j.split(" ")
    temperature[i] = [int(x) for x in temperature[i]]

## split humidity
humidity = humidity.split("\n")
humidity = humidity[1:]
for i, j in enumerate(humidity):
    humidity[i] = j.split(" ")
    humidity[i] = [int(x) for x in humidity[i]]

## split location
location = location.split("\n")
location = location[1:]
for i, j in enumerate(location):
    location[i] = j.split(" ")
    location[i] = [int(x) for x in location[i]]

###  dest start - source start - range
# convert seeds to soil
for i, seed in enumerate(seeds):
    for s in soil:
        if seed >= s[1] and seed < s[1] + s[2]-1:
            seeds[i] = s[0] + seed - s[1]

# convert soil to fertilizer
for i, seed in enumerate(seeds):
    for f in fertilizer:
        if seed >= f[1] and seed < f[1] + f[2]:
            seeds[i] = f[0] + seed - f[1]

# convert fertilizer to water
for i, seed in enumerate(seeds):
    for w in water:
        if seed >= w[1] and seed < w[1] + w[2]:
            seeds[i] = w[0] + seed - w[1]

# convert water to light
for i, seed in enumerate(seeds):
    for l in light:
        if seed >= l[1] and seed < l[1] + l[2]:
            seeds[i] = l[0] + seed - l[1]

# convert light to temperatur
for i, seed in enumerate(seeds):
    for t in temperature:
        if seed >= t[1] and seed < t[1] + t[2]:
            seeds[i] = t[0] + seed - t[1]

# convert temperature to humidity
for i, seed in enumerate(seeds):
    for h in humidity:
        if seed >= h[1] and seed < h[1] + h[2]:
            seeds[i] = h[0] + seed - h[1]

# convert humidity to location
for i, seed in enumerate(seeds):
    for l in location:
        if seed >= l[1] and seed < l[1] + l[2]:
            seeds[i] = l[0] + seed - l[1]

print(min(seeds))

