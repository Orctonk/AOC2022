import re
import math

f = open("2023/8/input.txt")

instructions = f.readline().strip()

nodes = {}

for l in f.readlines():
  m = re.match(r"(.+) = \((.+), (.+)\)",l)

  if m:
    nodes[m[1]] = (m[2],m[3])

curnode = "AAA"

i = 0
n = 0
while curnode != "ZZZ":
  ind = instructions[i]
  curnode = nodes[curnode][1 if ind == "R" else 0]

  i = (i+1) % len(instructions)
  n += 1

print(n)

print("Part 2")

i = 0
n = 0

curnodes = [n for n in nodes if n[2] == "A"]

counts = []

for node in curnodes:
  i = 0
  n = 0

  while node[2] != "Z":
    ind = 1 if instructions[i] == "R" else 0
    node = nodes[node][ind]

    i = (i+1) % len(instructions)
    n += 1

  counts.append(n)
  
print(math.lcm(*counts))