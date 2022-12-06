class Range:
    def __init__(self, rangeStr: str):
        mid = rangeStr.find("-")
        self.lower = int(rangeStr[0:mid])
        self.upper = int(rangeStr[mid+1:])

    def contains(self, other):
        return other.lower >= self.lower and other.upper <= self.upper

    def overlaps(self, other):
        return self.contains(other) or other.contains(self) or (self.lower >= other.lower and self.lower <= other.upper) or (self.upper >= other.lower and self.upper <= other.upper)


def parsePair(line: str):
    mid = line.find(",")
    r1 = line[0:mid]
    r2 = line[mid+1:]

    return (Range(r1), Range(r2))


f = open("4/input.txt")

total = 0
for l in f:
    (r1, r2) = parsePair(l)
    if r1.overlaps(r2):
        total += 1

print(total)
