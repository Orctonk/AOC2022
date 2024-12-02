f = open("2023/13/input.txt")

patterns = []

pattern = []
for l in f.readlines():
  if l != "\n":
    pattern.append(l.strip())
  else:
    patterns.append(pattern)
    pattern = []

patterns.append(pattern)

def checkReflection(items:str,point):
  first = list(reversed(items[0:point]))
  last = list(items[point:])
  
  minlen = min(len(first),len(last))
  return first[:minlen] == last[:minlen]

def fixSmudge(items:str, point):
  first = list(reversed(items[0:point]))
  last = list(items[point:])
  
  minlen = min(len(first),len(last))
  for i in range(minlen):
    if first[i] != last[i]:
      return (i + len(first) - minlen, last[i])

  return (0,"")

def findReflection(pattern, smudged = False):
  possible = range(1,len(pattern[0]))

  fixed = False
  if smudged:
    votes = []
    for r in pattern:
      votes.append([checkReflection(r,i) for i in range(1,len(pattern[0]))])

    votes = list(map(list, zip(*votes)))
    for i,r in enumerate(votes):
      if r.count(False) == 1:
        at = r.index(False)
        pattern[at] = fixSmudge(pattern[at],i+1)
        fixed = True
        break
  
  if not smudged or fixed: 
    for r in pattern:
      possible = list(filter(lambda p: checkReflection(r,p), possible))

    possible = list(possible)
    if len(possible) > 0:
      return possible[0]

  assert not fixed
  fixed = False
  if smudged:
    votes = []
    for c in range(len(pattern[0])):
      votes.append([checkReflection([l[c] for l in pattern],i) for i in range(1,len(pattern))])

    votes = list(map(list, zip(*votes)))
    for i,r in enumerate(votes):
      if r.count(False) == 1:
        at = r.index(False)
        pattern[at] = fixSmudge(pattern[at],i+1)
        fixed = True
        break
      if fixed:
        break

  possible = range(1,len(pattern))
  for c in range(len(pattern[0])):
    possible = list(filter(lambda p: checkReflection([l[c] for l in pattern],p), possible))

  possible = list(possible)
  if len(possible) > 0:
    return 100*possible[0]
  
  assert False

summed = 0

for p in patterns:
  summed += findReflection(p)

print(summed)
print("Part 2")

summed = 0

for p in patterns:
  summed += findReflection(p,True)

print(summed)