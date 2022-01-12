dots = []
folds = []
with open("Day 13 Input.txt") as data:
    line = data.readline()
    while line!="\n":
        dot = line.split(",")
        dots.append([int(dot[0]),int(dot[1])])
        line = data.readline()
    for line in data:
        fold = line.split()[-1]
        d,n = fold.split("=")
        folds.append((d,int(n)))

width = 0
height = 0
for fold in folds:
    line = fold[1]
    newDots = []
    for x,y in dots:
        newDot = [x,y]
        if fold[0] == "x":
            newDot[0] = line - abs(line - x)
            width = line
        else:
            newDot[1] = line - abs(line - y)
            height = line
        if newDot not in newDots:
            newDots.append(newDot)
    dots = newDots

out = [[" " for x in range(width)] for y in range(height)]
for dot in dots:
    out[dot[1]][dot[0]] = "#"
for row in out:
    print("".join(row))
