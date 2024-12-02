f = open("8/input.txt")

grid = [[int(c) for c in l.strip()] for l in f.readlines()]

visGrid = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]


def isVisible(grid, x, y):
    height = grid[y][x]
    for xc in range(0, x):
        if grid[y][xc] >= height:
            break
    else:
        return True
    for xc in range(x+1, len(grid[0])):
        if grid[y][xc] >= height:
            break
    else:
        return True

    for yc in range(0, y):
        if grid[yc][x] >= height:
            break
    else:
        return True

    for yc in range(y+1, len(grid)):
        if grid[yc][x] >= height:
            break
    else:
        return True

    return False


def populateVisGrid(grid, visGrid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            visGrid[y][x] = isVisible(grid, x, y)


def getScenicScore(grid, x, y):
    height = grid[y][x]
    left = 0
    for xc in range(x-1, -1, -1):
        left += 1
        if grid[y][xc] >= height:
            break
    right = 0
    for xc in range(x+1, len(grid[0])):
        right += 1
        if grid[y][xc] >= height:
            break
    up = 0
    for yc in range(y-1, -1, -1):
        up += 1
        if grid[yc][x] >= height:
            break
    down = 0
    for yc in range(y+1, len(grid)):
        down += 1
        if grid[yc][x] >= height:
            break

    return left * right * up * down


populateVisGrid(grid, visGrid)

maxScore = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        score = getScenicScore(grid, x, y)
        maxScore = max(score, maxScore)

print(maxScore)
