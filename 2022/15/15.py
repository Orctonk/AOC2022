import re

class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def contains(self, other):
        return other.lower >= self.lower and other.upper <= self.upper

    def overlaps(self, other):
        return self.contains(other) or other.contains(self) or (self.lower >= other.lower and self.lower <= other.upper) or (self.upper >= other.lower and self.upper <= other.upper)
    
    def merge(self,other):
      if self.contains(other):
        return self
      if other.contains(self):
        return other
      if self.lower >= other.lower and self.lower <= other.upper + 1:
        return Range(other.lower,self.upper)
      if self.upper >= other.lower-1 and self.upper <= other.upper:
        return Range(self.lower, other.upper)
      
      # Couldn't merge
      return None

beacons = []

f = open("15/input.txt")

reg = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

for l in f:
  m = reg.match(l)
  pos = (int(m[1]),int(m[2]))
  closest = (int(m[3]),int(m[4]))
  distance = abs(pos[0] - closest[0]) + abs(pos[1] - closest[1])
  beacons.append((pos,distance))

def findGap(sensors, ytarget):
  xBounds = []
  for b in sensors:
    ydiff = abs(b[0][1] - ytarget)
    if ydiff > b[1]:
      continue
    span = b[1] - ydiff
    xBounds.append(Range(b[0][0] - span, b[0][0] + span))

  merge = True

  while merge:
    merge = False
    old = xBounds
    xBounds = []
    for i in range(len(old)):
      if i >= len(old):
        break
      for j in range(i+1, len(old)):
        merged = old[i].merge(old[j])
        if merged is not None:
          merge = True
          xBounds.append(merged)
          old[i] = merged
          old.pop(j)
          break
      else:
        xBounds.append(old[i])
    
  contained = False
  testRange = Range(0,4000000)
  for b in xBounds:
    if b.contains(testRange):
      contained = True
      break

  if contained:
    return None
  
  return True

for y in range(0,4000000):
  if y % 100000 == 0:
    print(f"Iteration {y}")
  if findGap(beacons,y) is not None:
    print(y)
