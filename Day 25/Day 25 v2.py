def moveHerds(herds, dimensions):
    newHerds = (set(), set())
    moved = False
    for d, herd in enumerate(herds):
        for c in herd:
            move = (c[0] if d else (c[0] + 1 if c[0] < dimensions[0] - 1 else 0),
                    (c[1] + 1 if c[1] < dimensions[1] - 1 else 0) if d else c[1])
            if move in (herds[0], newHerds[0])[d] or move in herds[1]:
                newHerds[d].add(c)
            else:
                newHerds[d].add(move)
                moved = True
    return newHerds, moved


def getHerds():
    with open("Day 25 Input.txt") as data:
        dataList = list(data)
        dimensions = (len(dataList[0]) - 1, len(dataList))
        herds = (set(), set())
        for y, row in enumerate(dataList):
            for x, c in enumerate(row.strip()):
                if c != ".":
                    herds[">v".index(c)].add((x, y))
        return herds, dimensions


def printHerds(herds, dimensions):
    grid = [list("." * dimensions[0]) for i in range(dimensions[1])]
    for d, herd in enumerate(herds):
        for x, y in herd:
            grid[y][x] = ">v"[d]
    print("Cucumbers:")
    [print("".join(row)) for row in grid]
    print()


def main():
    herds, dimensions = getHerds()
    moved = True
    steps = 0
    while moved:
        herds, moved = moveHerds(herds, dimensions)
        steps += 1
    print(f"Total steps: {steps}")
    printHerds(herds, dimensions)


if __name__ == "__main__":
    main()
