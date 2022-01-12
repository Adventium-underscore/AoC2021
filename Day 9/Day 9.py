HEIGHTMAP = []
with open("Day 9 Input.txt") as data:
    for line in data:
        HEIGHTMAP.append([int(h) for h in line.strip()])
WIDTH = len(HEIGHTMAP[0])
LENGTH = len(HEIGHTMAP)


def getAdjacent(x, y):
    points = []
    for xOffset, yOffset in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= xOffset < WIDTH and 0 <= yOffset < LENGTH:
            points.append((HEIGHTMAP[yOffset][xOffset], (xOffset, yOffset)))
    return points


def findBasin(x, y, basin):
    adjacent = getAdjacent(x, y)
    new = {p for p in adjacent if p[0] != 9}.difference(basin)
    basin = basin.union(new)
    for h, p in new:
        basin = basin.union(findBasin(p[0], p[1], basin))
    return basin


basins = []
for y, row in enumerate(HEIGHTMAP):
    for x, height in enumerate(row):
        adjacent = getAdjacent(x, y)
        lower = [p for p in adjacent if p[0] <= height]
        if not lower:
            basin = findBasin(x, y, {(height, (x, y))})
            basins.append(len(basin))

basins.sort()
basins.reverse()
total = basins[0] * basins[1] * basins[2]
print(total)
