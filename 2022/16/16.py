import re
import numpy as np

f = open("16/input.txt")
reg = re.compile("Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves?")

ValveInd = {}
np.array([])

def addConnection(v1, v2, length):
  global Connections
  if v1 == v2:
    return

  for i,c in enumerate(Connections[v1]):
    if c[0] == v2:
      Connections[v1][i] = (c[0],min(length,c[1]))
      break
  else:
    Connections[v1].append((v2,length))
    
  for i,c in enumerate(Connections[v2]):
    if c[0] == v1:
      Connections[v2][i] = (c[0],min(length,c[1]))
      break
  else:
    Connections[v2].append((v1,length))
  
valves = []
connections = {}
for l in f:
  m = reg.match(l)
  valves.append((m[1],int(m[2])))
  connections.union({tuple(sorted((m[1],c.strip())) + (1,)) for c in l[m.span()[1]:].split(",")})

valvesToRemove = []

for v in valves:
  if v[1] == 0 and v[0] != "AA":
    valvesToRemove.append(v)

    for c1 in Connections[v]:
      for c2 in Connections[v]:
        addConnection(c1[0],c2[0],c1[1] + c2[1])

for v in valvesToRemove:
  Valves.pop(v)
  Connections.pop(v)
  for c in Connections:
    Connections[c] = [con for con in Connections[c] if con[0] != v]

print(Valves)
print(Connections)

def maxPressureRelease(valves, conns, pos, open, timeLeft):
  if timeLeft < 0:
    return 0
  
  releasePerMin = sum([valves[v] for v in open])
  best = releasePerMin * timeLeft
  
  # Open
  if not pos in open:
    best = releasePerMin + maxPressureRelease(valves,conns,pos,open.union({pos}), timeLeft - 1)

  # Move
  for c in Connections[pos]:
    if c[1] < timeLeft and not c[0] in open:
      best = max(best, c[1] * releasePerMin + maxPressureRelease(valves, conns, c[0], open, timeLeft - c[1]))

  return best

print(maxPressureRelease(Valves,Connections,"AA",set(),30))