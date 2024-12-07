f = open("3/input.txt")


def charPrio(char):
    val = ord(char)
    if val < ord('a'):
        return val - ord('A') + 27
    else:
        return val - ord('a') + 1


def getPrio(rucksack):
    mid = int(len(rucksack)/2)
    comp1 = rucksack[0:mid]
    comp2 = rucksack[mid:]

    for c in comp1:
        if c in comp2:
            return charPrio(c)


def getGroupPrio(e1, e2, e3):
    for c in e1:
        if c in e2 and c in e3:
            return charPrio(c)


total = 0
inp = [l.strip() for l in f]
for i in range(0, len(inp), 3):
    total += getGroupPrio(inp[i], inp[i+1], inp[i+2])

print(total)
