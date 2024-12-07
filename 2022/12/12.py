f = open("12/input.txt")

map = []
distanceMap = []

start = (0,0)
end = (0,0)

for l in f:
  map.append([])
  distanceMap.append([])
  for c in l.strip():
    if c == "S":
      start = (len(map[-1]), len(map) - 1)
      map[-1].append(0)
      distanceMap[-1].append(100000)
    elif c == "E":
      end = (len(map[-1]), len(map) - 1)
      map[-1].append(ord("z") - ord("a"))
      distanceMap[-1].append(0)
    else:
      map[-1].append(ord(c) - ord("a"))
      distanceMap[-1].append(100000)

queue = [end]

def checkAdd(pos, queue, height, distanceMap, distance):
  if pos[0] < 0 or pos[0] >= len(map[0]) or pos[1] < 0 or pos[1] >= len(map):
    return
  if height - map[pos[1]][pos[0]] < 2:
    if distance < distanceMap[pos[1]][pos[0]]:
      distanceMap[pos[1]][pos[0]] = distance
      queue.append(pos)

while len(queue) != 0:
  pos = queue.pop()
  height = map[pos[1]][pos[0]]
  distance = distanceMap[pos[1]][pos[0]] + 1
  checkAdd((pos[0] + 1, pos[1]),queue,height,distanceMap, distance)
  checkAdd((pos[0] - 1, pos[1]),queue,height,distanceMap, distance)
  checkAdd((pos[0], pos[1] + 1),queue,height,distanceMap, distance)
  checkAdd((pos[0], pos[1] - 1),queue,height,distanceMap, distance)

minSteps = 10000

for y in range(len(map)):
  for x in range(len(map[0])):
    if map[y][x] == 0:
      minSteps = min(minSteps,distanceMap[y][x])

print(minSteps)