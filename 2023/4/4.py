f = open("2023/4/input.txt")

def parseCard(txt: str):
  txt = txt.strip()
  colon = txt.find(":")
  pipe = txt.find("|")
  no = int(txt[4:colon].strip())

  winlist = txt[colon+1:pipe].split(" ")
  winning = [int(t) for t in winlist if t.isdigit()]
  actlist = txt[pipe + 1:].split(" ")
  actual = [int(t) for t in actlist if t.isdigit()]

  return no, winning, actual

lines = f.readlines()
copies = [1] * len(lines)
points = 0

for i,l in enumerate(lines):
  no,winning,actual = parseCard(l)

  wins = 0
  for a in actual:
    if a in winning:
      wins += 1

  if wins > 0:
    points += 2 ** (wins-1)

  for n in range(wins):
    copies[i+1+n] += copies[i]

print(points)
print("Part 2")
print(sum(copies))