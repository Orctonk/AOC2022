f = open("2023/10/input.txt")

grid = [l.strip() for l in f.readlines() ]

start = (-1,-1)
for y in range(len(grid)):
  for x in range(len(grid[y])):
    if grid[y][x] == "S":
      start = (x,y)

queue = [(start,0)]
done = {}

def replaceStart(pos, grid):
  neigh = []
  x,y = pos
  if grid[y+1][x] in ["J","L","|"]:
    neigh.append((x,y+1))
  if grid[y-1][x] in ["F","7","|"]:
    neigh.append((x,y-1))
  if grid[y][x+1] in ["J","7","-"]:
    neigh.append((x+1,y))
  if grid[y][x-1] in ["F","L","-"]:
    neigh.append((x-1,y))

  repchar = "S"
  if (x+1,y) in neigh and (x-1,y) in neigh:
    repchar = "-"
  if (x,y+1) in neigh and (x,y-1) in neigh:
    repchar = "|"
  if (x+1,y) in neigh and (x,y-1) in neigh:
    repchar = "L"
  if (x+1,y) in neigh and (x,y+1) in neigh:
    repchar = "F"
  if (x-1,y) in neigh and (x,y-1) in neigh:
    repchar = "J"
  if (x-1,y) in neigh and (x,y+1) in neigh:
    repchar = "7"

  grid[y] = grid[y].replace("S",repchar)
  
replaceStart(start,grid)



def getNeighbours(pos,grid):
  x,y = pos
  shape = grid[y][x]
  if shape == "L":
    return [(x, y-1),(x+1,y)]
  elif shape == "|":
    return [(x, y-1),(x,y+1)]
  elif shape == "-":
    return [(x-1, y),(x+1,y)]
  elif shape == "J":
    return [(x-1,y),(x,y-1)]
  elif shape == "7":
    return [(x-1,y),(x,y+1)]
  elif shape == "F":
    return [(x+1,y),(x,y+1)]

while len(queue) > 0:
  pos,dist = queue.pop(0)

  if not pos in done:
    done[pos] = dist

    for n in getNeighbours(pos,grid):
      queue.append((n,dist + 1))

maxsteps = max([done[d] for d in done])

print(maxsteps)

print("Part 2")

numinside = 0
for y in range(len(grid)):
  inside = False
  up = None
  for x in range(len(grid[y])):
    if (x,y) in done:
      print(grid[y][x],end="")

      if grid[y][x] == "|":
        inside = not inside
      elif grid[y][x] == "F":
        up = False
      elif grid[y][x] == "L":
        up = True
      elif grid[y][x] == "J" and up == False:
        inside = not inside
      elif grid[y][x] == "7" and up == True:
        inside = not inside

    elif inside:
      numinside += 1
      print("I",end="")
    else:
      print("O",end="")

  print("")

print(numinside)