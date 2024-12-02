f = open("2023/3/input.txt")

grid = [l.strip() for l in f.readlines()]

mask = [[False] * len(g) for g in grid]

for y in range(len(grid)):
  for x in range(len(grid[y])):
    if grid[y][x].isdigit() or grid[y][x] == ".":
      continue
    
    for yoff in [-1,0,1]:
      for xoff in [-1,0,1]:
        if y + yoff < 0 or y + yoff >= len(mask):
          continue
        if x + xoff < 0 or x + xoff >= len(mask):
          continue

        mask[y+yoff][x+xoff] = True

nums = []
curnum = ""
curmask = False

for y in range(len(grid)):
  for x in range(len(grid[y])):
    if not grid[y][x].isdigit():
      if len(curnum) > 0 and curmask:
        nums.append(int(curnum))
      curnum = ""
      curmask = False
      continue
    else:
      curnum += grid[y][x]
      curmask = curmask or mask[y][x]

  if len(curnum) > 0 and curmask:
    nums.append(int(curnum))
  curnum = ""
  curmask = False

print(sum(nums))


print("Part 2:")

def getGear(x,y):
  minx = x
  while minx >= 0 and grid[y][minx].isdigit():
    minx -= 1
  maxx = x
  while maxx < len(grid[y]) and grid[y][maxx].isdigit():
    maxx += 1

  gear = int(grid[y][minx+1:maxx])
  used = range(minx+1,maxx)
  return gear,used

ratioSum = 0

for y in range(len(grid)):
  for x in range(len(grid[y])):
    if grid[y][x] == "*":
      gear1 = None
      gear2 = None
      used = []
      g1y = -1
      for yoff in [-1,0,1]:
        for xoff in [-1,0,1]:
          if y + yoff < 0 or y + yoff >= len(mask):
            continue
          if x + xoff < 0 or x + xoff >= len(mask):
            continue
          
          if y+yoff == g1y and x+xoff in used:
            continue

          if grid[y+yoff][x+xoff].isdigit():
            if gear1 == None:
              gear1, used = getGear(x+xoff, y + yoff)
              g1y = y+yoff
            else:
              gear2, _ = getGear(x+xoff,y+yoff)

      if gear1 and gear2:
        ratioSum += gear1 * gear2
      assert gear1 != gear2

print(ratioSum)