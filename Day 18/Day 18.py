def constructSnail(s):
    if len(s) == 1:
        return int(s)
    elif len(s) == 5:
        return [int(s[1]), int(s[3])]
    else:
        brackets = 1
        split = 2
        while brackets > 0:
            if s[split] == "[":
                brackets += 1
            elif s[split] == "]":
                brackets -= 1
            split += 1
        if split == len(s):
            return [int(s[1]), constructSnail(s[3:-1])]
        a = s[1:split]
        b = s[split+1:-1]
        return [constructSnail(a), constructSnail(b)]


def checkSnail(snail):
    if type(snail) == int:
        n = int(snail)
        return [(n if n > 9 else 0), []], [0, []]
    else:
        abig, adeep = checkSnail(snail[0])
        bbig, bdeep = checkSnail(snail[1])
        big = abig
        bpath = 0
        if bbig[0] and not abig[0]:
            big = bbig
            bpath = 1
        big[1].insert(0, bpath)

        deep = adeep
        dpath = 0
        if bdeep[0] > adeep[0]:
            deep = bdeep
            dpath = 1
        deep[1].insert(0, dpath)
        return [big[0], big[1]], [1 + deep[0], deep[1]]


def followPath(snail, path):
    out = snail
    for p in path:
        out = out[p]
    return out


def updateSnail(snail, path, value):
    if path:
        if path[0]:
            return [snail[0], updateSnail(snail[1], path[1:], value)]
        else:
            return [updateSnail(snail[0], path[1:], value), snail[1]]
    else:
        return value


def getAdjacentPath(snail, path):
    num = int("".join([str(n) for n in path]),2)
    left = []
    if 1 in path:
        leftFull = [int(c) for c in bin(num-1)[2:].zfill(len(path))]
        for p in leftFull:
            if type(followPath(snail, left)) == list:
                left.append(p)
    right = []
    if 0 in path:
        rightFull = [int(c) for c in bin(num+1)[2:].zfill(len(path))]
        rightFull.append(0)
        for p in rightFull:
            if type(followPath(snail, right)) == list:
                right.append(p)
    return left, right


def reduceSnail(snail):
    more = True
    while more:
        big, depth = checkSnail(snail)
        if depth[0] > 4:
            path = depth[1][:-1]
            deepest = followPath(snail, path)
            a, b = deepest
            pl, pr = getAdjacentPath(snail, path)
            if pl:
                left = followPath(snail, pl)
                snail = updateSnail(snail, pl, left + a)
            if pr:
                right = followPath(snail, pr)
                snail = updateSnail(snail, pr, right + b)
            snail = updateSnail(snail, path, 0)
        else:
            if big[0]:
                split = [big[0] // 2, big[0] // 2]
                if big[0] % 2:
                    split[1] += 1
                snail = updateSnail(snail, big[1], split)
            else:
                more = False
    return snail


def magnitude(snail):
    if type(snail) == int:
        return int(snail)
    else:
        return 3 * magnitude(snail[0]) + 2 * magnitude(snail[1])


snails = [constructSnail(line.strip()) for line in open("Day 18 Input.txt")]

# total = snails[0]
# for s in snails[1:]:
#     total = reduceSnail([total, s])
#
# print(magnitude(total))

big = 0
for s1 in snails:
    for s2 in snails:
        if s1 != s2:
            big = max(big, magnitude(reduceSnail([s1,s2])))
print(big)
