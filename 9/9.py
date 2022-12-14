f = open("9/input.txt")

rope = [(0, 0) for _ in range(10)]

visited = {(0, 0)}


def sign(val):
    return -1 if val < 0 else 1


def propagate(h, rope, visited):
    if len(rope) == 0:
        visited.add(h)
        return [h]

    xdiff = h[0] - rope[0][0]
    ydiff = h[1] - rope[0][1]

    if abs(xdiff) <= 1 and abs(ydiff) <= 1:
        return [h] + rope
    elif abs(xdiff) > 1 and ydiff == 0:
        rope[0] = (rope[0][0] + sign(xdiff), rope[0][1])
    elif xdiff == 0 and abs(ydiff) > 1:
        rope[0] = (rope[0][0], rope[0][1] + sign(ydiff))
    else:
        rope[0] = (rope[0][0] + sign(xdiff), rope[0][1] + sign(ydiff))

    return [h] + propagate(rope[0], rope[1:], visited)


dirMap = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for l in f:
    direction = dirMap[l[0]]
    steps = int(l.strip()[2:])
    for _ in range(steps):
        print(f"{rope[0]=} {rope[9]=}")
        rope[0] = (rope[0][0] + direction[0], rope[0][1] + direction[1])
        rope = propagate(rope[0], rope[1:], visited)

print(len(visited))
