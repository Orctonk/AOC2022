class Monkey:
  def __init__(self, lines):
    self.name = lines[0][0:-1]
    self.items = eval(f"[{lines[1][16:]}]")
    self.op = lines[2][16:]
    self.div = int(lines[3][18:])
    self.true = int(lines[4][-1])
    self.false = int(lines[5][-1])
    self.inspections = 0

  def process(self,monkeys, lcm):
    for old in self.items:
      self.inspections += 1
      new = eval(self.op)
      new = int(new % lcm)
      if new % self.div == 0:
        monkeys[self.true].items.append(new)
      else:
        monkeys[self.false].items.append(new)
    self.items = []
f = open("11/input.txt")

lines = [l.strip() for l in f]

monkeys = []
for l in range(0,len(lines),7):
  monkeys.append(Monkey(lines[l:l+6]))

lcm = 1
for m in monkeys:
  lcm *= m.div

for i in range(10000):
  for m in monkeys:
    m.process(monkeys, lcm)

inspections = []
for m in monkeys:
  print(f"{m.name}: {m.inspections}")
  inspections.append(m.inspections)

inspections.sort(reverse=True)
print(inspections[0] * inspections[1])