import re

f = open("19/input.txt")

class Blueprint:
  def __init__(self,text):
    reg = re.compile("Blueprint (\d+): (.*)\. (.*)\. (.*)\. (.*)\.")
    m = reg.match(text)
    self.id = int(m[1])
    self.oreCost = Blueprint.parseCost(m[2])
    self.clayCost = Blueprint.parseCost(m[3])
    self.obsidianCost = Blueprint.parseCost(m[4])
    self.geodeCost = Blueprint.parseCost(m[5])

    self.geodeValue = 100000
    self.obsidianValue = self.geodeCost[2]
    self.clayValue = self.geodeCost[1] + self.obsidianCost[1] * self.obsidianValue
    self.oreValue = self.geodeCost[0] + self.obsidianCost[0] * self.obsidianValue + self.clayCost[0] * self.clayValue
  
  def parseCost(line):
    ore = re.search("(\d+) ore", line)
    clay = re.search("(\d+) clay", line)
    obsidian = re.search("(\d+) obsidian", line)

    return (int(ore[1]) if ore else 0,int(clay[1]) if clay else 0,int(obsidian[1]) if obsidian else 0)

  def canBuild(self, cost, resources):
    for i in range(0,3):
      if cost[i] > resources[i]:
        return False
    return True

blueprints = []

for l in f:
  blueprints.append(Blueprint(l.strip()))

def getMaxGeodes(blueprint: Blueprint, timeleft, resources, robots):
  if timeleft == 0:
    return resources[3]
  
  possibilities = []

  if blueprint.canBuild(blueprint.oreCost,resources):
    newRes = [resources[i] - blueprint.oreCost[i] for i in range(3)]
    newRes.append(resources[-1])
    newRob = [r for r in robots]
    newRob[0] += 1
    possibilities.append((blueprint.oreValue / (robots[0] + 1), newRes,newRob))
  
  if blueprint.canBuild(blueprint.clayCost,resources):
    newRes = [resources[i] - blueprint.clayCost[i] for i in range(3)]
    newRes.append(resources[-1])
    newRob = [r for r in robots]
    newRob[1] += 1
    possibilities.append((blueprint.clayValue / (robots[1] + 1), newRes,newRob))

  if blueprint.canBuild(blueprint.obsidianCost,resources):
    newRes = [resources[i] - blueprint.obsidianCost[i] for i in range(3)]
    newRes.append(resources[-1])
    newRob = [r for r in robots]
    newRob[2] += 1
    possibilities.append((blueprint.obsidianValue / (robots[2] + 1), newRes,newRob))

  if blueprint.canBuild(blueprint.geodeCost,resources):
    newRes = [resources[i] - blueprint.geodeCost[i] for i in range(3)]
    newRes.append(resources[-1])
    newRob = [r for r in robots]
    newRob[3] += 1
    possibilities.append((blueprint.geodeValue, newRes,newRob)) 

  resources = [resources[i] + robots[i] for i in range(4)]

  maxPos = (0, resources, robots)
  for p in possibilities:
    if p[0] > maxPos[0]:
      maxPos = p

  return getMaxGeodes(blueprint,timeleft -1, maxPos[1], maxPos[2])

print(getMaxGeodes(blueprints[0],24,(0,0,0,0),(1,0,0,0)))