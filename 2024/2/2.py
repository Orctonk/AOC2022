f = open("2024/2/input.txt")

inp = []

def sign(i):
  return 1 if i > 0 else -1 if i < 0 else 0

def unsafe(diff, sig) -> bool:
  return abs(diff) > 3 or diff == 0 or sign(diff) != sig

for l in f.readlines():
  inp.append([int(i) for i in l.strip().split(" ")])

numSafe = 0
for report in inp:
  diffs = [report[i] - report[i+1] for i in range(len(report)-1)]
  sig = sign(sum([sign(d) for d in diffs]))
  if not any(map(lambda d: unsafe(d,sig), diffs)):
    numSafe += 1

print(numSafe)

numSafe = 0

for rnum, report in enumerate(inp):
  diffs = [report[i] - report[i+1] for i in range(len(report)-1)]
  sig = sign(sum([sign(d) for d in diffs]))
  numBad = 0
  
  skip = False
  for i in range(len(diffs)):
    if skip:
      skip = False
      continue
    if unsafe(diffs[i], sig):
      numBad += 1
      if i + 1 == len(diffs) or not unsafe(diffs[i] + diffs[i+1], sig):
        skip = True
        pass
      elif i == 0 or not unsafe(diffs[i-1] + diffs[i], sig):
        pass
      else:
        print("Unrecoverable")
        numBad += 100
  if numBad <= 1:
    numSafe += 1
  else:
    print(rnum)
print(numSafe)