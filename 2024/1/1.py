f = open("2024/1/input.txt")

l1 = []
l2 = []

for l in f.readlines():
  l = l.strip()
  center = l.find(" ")
  l1.append(int(l[:center]))
  l2.append(int(l[center:]))

l1.sort()
l2.sort()

tot = 0
for i1,i2 in zip(l1,l2):
  tot += abs(i1 - i2)

print(tot)

occs = {}
for i in l2:
  if i in occs:
    occs[i] = occs[i] + 1
  else: 
    occs[i] = 1

tot = 0
for i in l1:
  multip = occs.get(i,0)
  tot += multip * i

print(tot)