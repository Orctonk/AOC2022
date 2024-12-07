import re

f = open("2024/7/input.txt")

inp = []

pat = re.compile(r'(\d+): (.+)')

for l in f.readlines():
  m = pat.match(l)
  inp.append([int(m[1])] + [int(i) for i in m[2].split(" ")])

def valid(target, cur, inputs):
  if cur > target:
    return False
  if len(inputs) == 0:
    return cur == target
  ops = [lambda a,b: a + b, lambda a,b: a *b, lambda a,b: int(str(a) + str(b))]

  for op in ops:
    if valid(target, op(cur,inputs[0]),inputs[1:]):
      return True
  return False

tot = 0
for i in inp:
  tar = i[0]
  if valid(tar,i[1],i[2:]):
    tot += tar

print(tot)