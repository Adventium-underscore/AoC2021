def moveEast(east, south, width):
    newEast = set()
    moved = False
    for c in east:
        move = (c[0] + 1 if c[0] < width - 1 else 0, c[1])
        if move in east or move in south:
            newEast.add(c)
        else:
            newEast.add(move)
            moved = True
    return newEast, moved


def moveSouth(east, south, height):
    newSouth = set()
    moved = False
    for c in south:
        move = (c[0], c[1] + 1 if c[1] < height - 1 else 0)
        if move in east or move in south:
            newSouth.add(c)
        else:
            newSouth.add(move)
            moved = True
    return newSouth, moved


def getHerds():
    with open("Day 25 Input.txt") as data:
        dataList = list(data)
        width = len(dataList[0]) - 1
        height = len(dataList)
        east = set()
        south = set()
        for y, row in enumerate(dataList):
            for x, c in enumerate(row.strip()):
                if c == ">":
                    east.add((x, y))
                elif c == "v":
                    south.add((x, y))
        return east, south, width, height


def printHerds(east, south, width, height):
    grid = [["." for j in range(width)] for i in range(height)]
    for x, y in east:
        grid[y][x] = ">"
    for x, y in south:
        grid[y][x] = "v"
    print("Cucumbers:")
    [print("".join(row)) for row in grid]
    print()


def main():
    east, south, width, height = getHerds()
    eastMoved = southMoved = True
    steps = 0
    while eastMoved or southMoved:
        east, eastMoved = moveEast(east, south, width)
        south, southMoved = moveSouth(east, south, height)
        steps += 1
    print(f"Total steps: {steps}")
    printHerds(east, south, width, height)


if __name__ == "__main__":
    main()
