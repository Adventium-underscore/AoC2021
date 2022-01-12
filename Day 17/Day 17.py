targetInput = open("Day 17 Input.txt").readline().strip()[13:].split(", ")
targetX = list(map(int,targetInput[0][2:].split("..")))
targetY = list(map(int,targetInput[1][2:].split("..")))
targetY.reverse()


def testTrajectory(vx, vy):
    x = y = 0
    while x < targetX[1] and y > targetY[1]:
        x += vx
        y += vy
        if vx: vx -= 1
        vy -= 1
        if targetX[0] <= x <= targetX[1] and targetY[0] >= y >= targetY[1]:
            return True
    return False


lastHit = (targetX[1], targetY[1])
hits = {lastHit}
for x in range(targetX[1],0,-1):
    y = lastHit[1]
    missCount = 0
    errorCap = abs(targetY[1] - targetY[0])
    i = 0
    while missCount < errorCap:
        if testTrajectory(x, y + i):
            hits.add((x, y + i))
            lastHit = (x, y + i)
            missCount = 0
        else:
            missCount += 1
        if testTrajectory(x, y - i):
            hits.add((x, y - i))
            missCount = 0
        i += 1

print(len(hits))

