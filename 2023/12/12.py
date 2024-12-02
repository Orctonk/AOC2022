import functools
f = open("2023/12/input.txt")

records= []
for l in f.readlines():
  damaged, contiguous = l.strip().split(" ")
  cont_list = tuple([ int(i) for i in contiguous.split(",")])
  records.append((damaged, cont_list))

@functools.lru_cache()
def resolve(damaged:str,contiguous,lb = 0):

  if len(contiguous) == 0:
    return 1 if damaged.find("#", lb) == -1 else 0
  
  end = sum(contiguous[1:])
  end += len(contiguous) - 1

  tograb = contiguous[0]

  numRes = 0
  ub = len(damaged) - end - tograb + 1
  first = damaged.find("#",lb)
  if first != -1:
    ub = min(ub,first+1)

  for i in range(lb,ub):
    contains = damaged.find(".",i,i+tograb) != -1
    if contains or (i+tograb < len(damaged) and damaged[i+tograb] == "#"):
      continue
    else:
      numRes += resolve(damaged,contiguous[1:],i+tograb+1)

  return numRes

resSum = 0

# for r in records:
#   resSum += resolve(r[0],r[1])

# print(resSum)
print("Part 2")
records = [(((r[0] + "?")*5)[:-1],r[1 ]*5) for r in records]
resSum = 0

for r in records:
  resSum += resolve(r[0],r[1])

print(resSum)