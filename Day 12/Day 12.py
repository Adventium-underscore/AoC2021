LINKS = [l.strip().split("-") for l in open("Day 12 Input.txt")]


def recurse(paths):
    newPaths = []
    for path, extra in paths:
        end = path[-1]
        if end=="end":
            newPaths.append(path)
        else:
            caves = []
            for link in LINKS:
                if end in link:
                    l = link.copy()
                    l.remove(end)
                    caves.append(l[0])
            for cave in caves:
                if cave != "start":
                    if cave.islower() and cave in path:
                        if not extra:
                            p = path.copy()
                            p.append(cave)
                            newPaths.extend(recurse([[p, True]]))
                    else:
                        p = path.copy()
                        p.append(cave)
                        newPaths.extend(recurse([[p, extra]]))
    return newPaths


routes = recurse([[["start"], False]])
# [print(r) for r in routes]
print("Total: " + str(len(routes)))
