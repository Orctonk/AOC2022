f = open("2023/11/input.txt")

galaxies = []

y_pop = set({})
x_pop = set({})

for y,l in enumerate(f.readlines()):
  for x,c in enumerate(l):
    if c == "#":
      y_pop.add(y)
      x_pop.add(x)
      galaxies.append((x,y))

y_list = [y for y in range(0,max(y_pop)) if not y in y_pop]
x_list = [x for x in range(0,max(x_pop)) if not x in x_pop]

def getOffsetPosition(galaxy,x_space,y_space,expansion=1):
  y_off = 0
  for y in y_space:
    if y < galaxy[1]:
      y_off += expansion

  x_off = 0
  for x in x_space:
    if x < galaxy[0]:
      x_off += expansion

  return galaxy[0] + x_off, galaxy[1] + y_off

exp_galaxies = [getOffsetPosition(g,x_list,y_list) for g in galaxies ]

summed_dist = 0

for i in range(len(exp_galaxies)):
  g1 = exp_galaxies[i]
  for j in range(i+1,len(exp_galaxies)):
    g2 = exp_galaxies[j]
    dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
    summed_dist += dist

print(summed_dist)
print("Part 2")

exp_galaxies = [getOffsetPosition(g,x_list,y_list,1000000-1) for g in galaxies ]

summed_dist = 0

for i in range(len(exp_galaxies)):
  g1 = exp_galaxies[i]
  for j in range(i+1,len(exp_galaxies)):
    g2 = exp_galaxies[j]
    dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
    summed_dist += dist
print(summed_dist)