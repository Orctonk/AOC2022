import regex


def move(num, src, dst, stacks):
    stacks[dst].extend(stacks[src][-num:])
    for i in range(num):
        stacks[src].pop()


f = open("5/input.txt")
moveExp = regex.compile("move (\d+) from (\d+) to (\d+)")

stacks = []
stacksCreated = False
for l in f:
    if l == "\n":
        for s in stacks:
            s.reverse()
        stacksCreated = True
        continue
    if not stacksCreated:
        next = l.find("[")
        while next != -1:
            crate = l[next+1]
            stackIndex = int(next/4)
            while len(stacks) <= stackIndex:
                stacks.append([])

            stacks[stackIndex].append(crate)
            next = l.find("[", next + 1)
    else:
        m = moveExp.match(l)
        move(int(m[1]),int(m[2]) - 1,int(m[3]) - 1, stacks)


for s in stacks:
    print(s[-1],end="")
print("\n")
