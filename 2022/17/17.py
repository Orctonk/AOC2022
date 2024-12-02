import math
f = open("17/input.txt")

class Rock:
  HORI = 0
  PLUS = 1
  J = 2
  VERT = 3
  BOX = 4

  shapes = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(1,0),(1,1),(0,1),(2,1),(1,2)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(0,1),(1,0),(1,1)]
  ]

  def __init__(self, shape, height):
    self.shape = Rock.shapes[shape]
    self.width = max(self.shape,key=lambda s: s[0])[0]
    self.position = (2,height + 3)
  
  def move(self, dir, stack):
    newPos = (self.position[0] + dir[0],self.position[1] + dir[1])
    for s in self.shape:
      newX = s[0] + newPos[0]
      newY = s[1] + newPos[1]
      if newX < 0 or newX > 6 or newY < 0 or stack[newY][newX]:
        return False
    self.position = newPos
    return True

def listRepeats(list):
  return list[0:int(len(list)/2)] == list[int(len(list)/2):]

print(listRepeats([0,1,0]))

stack = []

dirs = f.readline().strip()

firstFree = 0
type = 0
stream = 0

diffs = []
loopFound = False

i = 0
while not loopFound:
  while len(stack) < firstFree + 7:
    stack.append([False for _ in range(7)])

  rock = Rock(type,firstFree)

  done = False

  while not done:
    rock.move((1,0) if dirs[stream] == ">" else (-1,0), stack)
    stream = (stream + 1) % len(dirs)
    done = not rock.move((0,-1),stack)

  type = (type + 1) % 5
  for s in rock.shape:
    stack[s[1] + rock.position[1]][s[0] + rock.position[0]] = True

  for j in range(firstFree,len(stack)):
    if not (True in stack[j]):
      if(i > 2000):
        diffs.append(j - firstFree)
        if diffs[0:int(len(diffs)/2)] == diffs[int(len(diffs)/2):]:
          loopFound = True
      firstFree = j
      break
  i += 1

target = 1000000000000
left = (target - i)
extra = int(left / len(diffs))
firstFree += sum(diffs) * extra
left = left - len(diffs) * extra
for i in range(left):
  firstFree += diffs[i]
print(firstFree)