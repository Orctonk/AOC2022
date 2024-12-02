f = open("2023/9/input.txt")

values = [[int(i) for i in l.strip().split(" ")] for l in f.readlines()]

def getDiffs(inp):
  return [inp[i] - inp[i - 1] for i in range(len(inp)) if i != 0]

totsum = 0

for v in values:
  diffs = []
  diffs.append(v)
  thisdiff = getDiffs(v)
  while any(thisdiff):
    diffs.append(thisdiff)
    thisdiff = getDiffs(thisdiff)

  diffs.append(thisdiff)

  diffs[-1].append(0)
  for i in range(1,len(diffs)):
    diffs[-(i+1)].append(diffs[-(i+1)][-1] + diffs[-i][-1])

  totsum += diffs[0][-1]

print(totsum)

print("Part 2")

totsum = 0

for v in values:
  diffs = []
  diffs.append(v)
  thisdiff = getDiffs(v)
  while any(thisdiff):
    diffs.append(thisdiff)
    thisdiff = getDiffs(thisdiff)

  diffs.append(thisdiff)

  diffs[-1].append(0)
  for i in range(1,len(diffs)):
    l = [diffs[-(i+1)][0] - diffs[-i][0]]
    l.extend(diffs[-(i+1)])
    diffs[-(i+1)] = l

  totsum += diffs[0][0]

print(totsum)