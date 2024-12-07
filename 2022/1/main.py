f = open("input.txt")
elves = [0]

for l in f:
    if l == "\n":
        elves.append(0)
    else:
        elves[-1] += int(l)

elves.sort()
print(sum(elves[-3:]))
