import re

f = open("2023/5/input.txt")

sm = re.findall(r"(\d+\w+)", f.readline())
input = [int(s) for s in sm]

line = f.readline()
while line != "":
  while len(line) == 0 or not line[0].isdigit():
    line = f.readline()

  maps = []
  while len(line) > 0 and line[0].isdigit():
    mapnums = re.findall(r"(\d+)", line)
    s = int(mapnums[1])
    d = int(mapnums[0])
    l = int(mapnums[2])
    maps.append((s,d,l))
    line = f.readline()
  
  out = []
  for m in maps:
    s,d,l = m
    toRemove = []
    for i in input:
      mapped = i + (d-s) if i >= s and i < s+l else None
      if mapped:
        out.append(mapped)
        toRemove.append(i)
    
    input = [i for i in input if not i in toRemove]
  
  input.extend(out)

print(min(input))
print("Part 2")

f = open("2023/5/input.txt")

sm = re.findall(r"(\d+\w+)", f.readline())
raw = [int(s) for s in sm]
input = []
for i in range(0,len(raw),2):
  input.append((raw[i], raw[i] + raw[i+1]))

def mapRange(r, s,d,l):
  if s > r[1] or s + l < r[0]:
    return None
  
  start = max(s,r[0])
  end = min(s+l,r[1])

  unmapped = []
  if start != r[0]:
    unmapped.append((r[0],start-1))
  if end != r[1]:
    unmapped.append((end+1,r[1]))
  offset = d - s
  mapped = (start + offset, end + offset)
  return unmapped, mapped

line = f.readline()
while line != "":
  print("New Map")
  while len(line) == 0 or not line[0].isdigit():
    line = f.readline()

  maps = []
  while len(line) > 0 and line[0].isdigit():
    mapnums = re.findall(r"(\d+)", line)
    s = int(mapnums[1])
    d = int(mapnums[0])
    l = int(mapnums[2])
    maps.append((s,d,l))
    line = f.readline()
  
  out = []
  for m in maps:
    s,d,l = m
    toRemove = []
    for i in input:
      mapped = mapRange(i,s,d,l)
      if mapped:
        out.append(mapped[1])
        toRemove.append(i)
        input.extend(mapped[0])
    
    input = [i for i in input if not i in toRemove]
  
  input.extend(out)

print(min(map(lambda x: x[0], input)))