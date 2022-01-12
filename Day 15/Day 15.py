GRID = [[int(c) for c in line.strip()] for line in open("Day 15 Input.txt")]
WIDTH = len(GRID[0])
LENGTH = len(GRID)


for y,line in enumerate(GRID):
    newLine = line.copy()
    inc = line.copy()
    for i in range(4):
        inc = [n+1 if n<9 else 1 for n in inc]
        newLine.extend(inc)
    GRID[y] = newLine
for i in range(4):
    newRows = []
    for y in range(LENGTH):
        yOffset = LENGTH * i + y
        newRows.append([n+1 if n<9 else 1 for n in GRID[yOffset]])
    GRID.extend(newRows)
WIDTH = len(GRID[0])
LENGTH = len(GRID)


def getAdjacent(x, y):
    points = []
    for xOffset, yOffset in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= xOffset < WIDTH and 0 <= yOffset < LENGTH:
            points.append((GRID[yOffset][xOffset], xOffset, yOffset))
    return points


cost = [[0 for x in range(WIDTH)] for y in range(LENGTH)]
checks = {(0,0)}
while checks:
    (x,y) = checks.pop()
    c = cost[y][x]
    for (nAdj,xAdj,yAdj) in getAdjacent(x,y):
        cAdj = cost[yAdj][xAdj]
        move = c+nAdj
        if move < cAdj or (not cAdj and (xAdj,yAdj)!=(0,0)):
            cost[yAdj][xAdj] = move
            checks.add((xAdj,yAdj))

print(cost[-1][-1])
