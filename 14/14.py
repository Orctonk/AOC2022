f = open("14/input.txt")

structures = []

maxy = 0

for l in f:
    delim = 0
    start = 0
    structures.append([])
    while delim != -1:
        delim = l.find("->", start)
        sub = l[start:delim]

        comma = sub.find(",")
        x = int(sub[0:comma])
        y = int(sub[comma+1:])
        maxy = max(y, maxy)

        structures[-1].append((x, y))

        start = delim + 2

map = [[0 for _ in range(0, 1000)]
       for _ in range(0, maxy+3)]

for i in range(1000):
    map[-1][i] = 1

for s in structures:
    for i in range(len(s) - 1):
        p1 = s[i]
        p2 = s[i+1]

        if p1[0] != p2[0] and p1[1] == p2[1]:
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                map[p1[1]][x] = 1

        elif p1[1] != p2[1] and p1[0] == p2[0]:
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                map[y][p1[0]] = 1

        else:
            print("Oops")

done = False
grains = 0
while not done:
    sand = (500, 0)
    move = True
    while move:
        if map[sand[1] + 1][sand[0]] == 0:
            sand = (sand[0], sand[1] + 1)
        elif map[sand[1] + 1][sand[0] - 1] == 0:
            sand = (sand[0] - 1, sand[1] + 1)
        elif map[sand[1] + 1][sand[0] + 1] == 0:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            map[sand[1]][sand[0]] = 2
            move = False
    grains += 1
    if sand[0] == 500 and sand[1] == 0:
        done = True


print(grains)
