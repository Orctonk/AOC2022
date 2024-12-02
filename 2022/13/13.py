from functools import cmp_to_key
f = open("13/input.txt")

l = f.readlines()
items = list(map(lambda i: i.strip(),filter(lambda i: i != "\n",l)))

pairs = []

for i in range(0, len(items),2):
  pairs.append((eval(items[i]),eval(items[i+1])))

def intComp(i1,i2):
  if i1 < i2:
    return 1
  elif i1 > i2:
    return -1
  else:
    return 0

def listComp(l1,l2):
  for i in range(min(len(l1),len(l2))):
    res = compPair(l1[i],l2[i])
    if res != 0:
      return res
  return intComp(len(l1),len(l2))

def compPair(p1,p2):
  i = 0.0

  if isinstance(p1,int) and isinstance(p2, int):
    return intComp(p1,p2)
  
  elif isinstance(p1,list) and isinstance(p2, list):
    return listComp(p1,p2)

  else:
    l1 = [p1] if isinstance(p1, int) else p1
    l2 = [p2] if isinstance(p2, int) else p2
    return listComp(l1,l2)

packets = []
for p in pairs:
  packets.append(p[0])
  packets.append(p[1])
packets.append([[2]])
packets.append([[6]])

packets.sort(key=cmp_to_key(compPair),reverse=True)

tot = 1
for i in range(0,len(packets)):
  if packets[i] == [[6]] or packets[i] == [[2]]:
    tot *= i+1
print(tot)