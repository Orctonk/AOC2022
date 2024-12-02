import re

f = open("2023/2/input.txt")

limits = {
  "red": 12,
  "green":13,
  "blue": 14
}

ids = 0
for l in f.readlines():
  game = re.search(r"Game (\d+):",l)
  id = int(game[1])
  found = []
  found.extend(re.findall(r"(\d+) (blue)",l))
  found.extend(re.findall(r"(\d+) (red)",l))
  found.extend(re.findall(r"(\d+) (green)",l))

  possible = True
  for f in found:
    if int(f[0]) > limits[f[1]]:
      possible = False
      break

  if possible:
    ids += id

print(ids)

print("Part 2:")

f = open("2023/2/input.txt")
powSum = 0
for l in f.readlines():
  game = re.search(r"Game (\d+):",l)
  id = int(game[1])
  found = []
  found.extend(re.findall(r"(\d+) (blue)",l))
  found.extend(re.findall(r"(\d+) (red)",l))
  found.extend(re.findall(r"(\d+) (green)",l))

  maxCubes = {
    "green" : 0,
    "red": 0,
    "blue": 0
  }

  for f in found:
    maxCubes[f[1]] = max(maxCubes[f[1]], int(f[0]))

  power = 1
  for v in maxCubes.values():
    power *= v
  powSum += power

print(powSum)