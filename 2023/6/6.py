import re
import math

def winSpan(time,distance):
  a = time/2
  b = math.sqrt(a**2 - distance)
  return (a-b,a+b)

f = open("2023/6/input.txt")

times = [int(t) for t in re.findall(r"(\d+)",f.readline())]
distances = [int(d) for d in re.findall(r"(\d+)",f.readline())]

races = zip(times,distances)

margin = 1

for race in races:
  w = winSpan(race[0],race[1])
  if int(w[0]) == w[0]:
    w = (w[0] + 0.01, w[1])
  if int(w[1]) == w[1]:
    w = (w[0], w[1] - 0.01)
  l = int(math.ceil(w[0]))
  u = int(math.floor(w[1]))

  numWins = u - l + 1
  margin *= numWins

print(margin)

print("Part 2")

f = open("2023/6/input.txt")

timestr = f.readline()
time = int(timestr[6:].strip().replace(" ", ""))
diststr = f.readline()
distance = int(diststr[10:].strip().replace(" ", ""))

w = winSpan(time,distance)
if int(w[0]) == w[0]:
  w = (w[0] + 0.01, w[1])
if int(w[1]) == w[1]:
  w = (w[0], w[1] - 0.01)
l = int(math.ceil(w[0]))
u = int(math.floor(w[1]))

numWins = u - l + 1
print(numWins)