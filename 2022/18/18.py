added = set()
neighbours = {}

f = open("18/input.txt")

for l in f:
  c1 = l.find(",")
  c2 = l.find(",",c1 + 1)

  x = int(l[0:c1])
  y = int(l[c1+1:c2])
  z = int(l[c2+1:])

  pos = (x,y,z)

  added.add(pos)
  if pos in neighbours:
    neighbours.pop(pos)

  def handleNeighbor(npos):
    if not npos in added:
      if npos in neighbours:
        neighbours[npos] += 1
      else:
        neighbours[npos] = 1

  for nx in range(x-1,x+2):
    if nx == x:
      continue
    handleNeighbor((nx,y,z))
  for ny in range(y-1,y+2):
    if ny == y:
      continue
    handleNeighbor((x,ny,z))
  for nz in range(z-1,z+2):
    if nz == z:
      continue
    handleNeighbor((x,y,nz))
    
inside = {}
def isInside(group,x,y,z):
  if (x,y,z) in inside:
    return inside[(x,y,z)]

total = 0
for v in neighbours.values():
  total += v

print(total)

