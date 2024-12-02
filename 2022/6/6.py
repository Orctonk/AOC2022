import re

f = open("6/input.txt")

stream = f.readline().strip()

pos = 0
for i in range(len(stream)):
    sub = stream[i:i+14]
    nomatch = True
    for (j, c1) in enumerate(sub):
        for c2 in sub[j+1:]:
            if c1 == c2:
                nomatch = False
    if nomatch:
        pos = i + 14
        break


print(pos)
