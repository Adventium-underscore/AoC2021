class Octo:
    flash = False
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy


OCTOS = []
with open("Day 11 Input.txt") as data:
    for y,line in enumerate(data):
        OCTOS.append([Octo(x,y,int(n)) for x,n in enumerate(line.strip())])
WIDTH = len(OCTOS[0])
LENGTH = len(OCTOS)
TOTAL = WIDTH * LENGTH


def getAdjacent(octo):
    adjacent = []
    for y in [octo.y + o for o in (-1,0,1)]:
        for x in [octo.x + o for o in (-1,0,1)]:
            if 0 <= x < WIDTH and 0 <= y < LENGTH:
                adjacent.append(OCTOS[y][x])
    adjacent.remove(octo)
    return adjacent


flashes = 0
step = 0
while flashes != TOTAL:
    flashes = 0
    step += 1
    check = []
    for row in OCTOS:
        for octo in row:
            octo.energy += 1
            if octo.energy > 9:
                check.append(octo)
    flashed = []
    while check:
        octo = check.pop()
        if not octo.flash and octo.energy > 9:
            octo.flash = True
            flashed.append(octo)
            for adjacent in getAdjacent(octo):
                adjacent.energy += 1
                check.append(adjacent)
    flashes += len(flashed)
    for octo in flashed:
        octo.energy = 0
        octo.flash = False

print("Synchro Step: " + str(step))