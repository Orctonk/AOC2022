class CPU:
  def __init__(self):
    self.cycles = 1
    self.X = 1
    self.busy = 0
    self.command = None

  def set(self, x):
    self.X = x

  def addx(self, val):
    self.busy = 2
    self.command = lambda: self.set(self.X + val)

  def noop(self):
    self.busy = 1

  def cycle(self):
    self.cycles += 1
    self.busy -= 1
    if self.busy == 0 and self.command is not None:
        self.command()
        self.command = None

  def strength(self):
    return self.X * self.cycles

c = CPU()

f = open("10/input.txt")

xpos = 0

for l in f:
  if l[0:4] == "noop":
    c.noop()
  elif l[0:4] == "addx":
    c.addx(int(l[5:].strip()))

  while c.busy != 0:
    print("#" if abs(c.X - xpos) < 2 else ".", end="")
    xpos += 1
    if xpos % 40 == 0 and xpos != 0:
      xpos = 0
      print("")
    c.cycle()
