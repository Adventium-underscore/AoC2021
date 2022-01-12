from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Cuboid:
    on: bool
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int


def countLights(cuboid):
    return cuboid.on * (cuboid.x2 - cuboid.x1 + 1) * (cuboid.y2 - cuboid.y1 + 1) * (cuboid.z2 - cuboid.z1 + 1)


def cuboidRef(cuboid, changes):
    cuboidDict = asdict(cuboid)
    cuboidDict.update(changes)
    return Cuboid(*cuboidDict.values())


def cutCuboid(cutter, cuboid) -> set[Cuboid]:
    if ((cuboid.x1 > cutter.x2 or cuboid.x2 < cutter.x1) or (cuboid.y1 > cutter.y2 or cuboid.y2 < cutter.y1)
            or (cuboid.z1 > cutter.z2 or cuboid.z2 < cutter.z1)):
        return {cuboid}
    else:
        bounds = {"x1": max(cuboid.x1, cutter.x1), "x2": min(cuboid.x2, cutter.x2),
                  "y1": max(cuboid.y1, cutter.y1), "y2": min(cuboid.y2, cutter.y2),
                  "z1": max(cuboid.z1, cutter.z1), "z2": min(cuboid.z2, cutter.z2)}
        bounded = cuboidRef(cutter, bounds)
        result = set()

        if cuboid.x1 < bounded.x1:
            result.add(cuboidRef(cuboid, {"x2": bounded.x1 - 1}))
        if bounded.x2 < cuboid.x2:
            result.add(cuboidRef(cuboid, {"x1": bounded.x2 + 1}))

        if cuboid.y1 < bounded.y1:
            result.add(cuboidRef(cuboid, {"x1": bounded.x1, "x2": bounded.x2,
                                          "y2": bounded.y1 - 1}))
        if bounded.y2 < cuboid.y2:
            result.add(cuboidRef(cuboid, {"x1": bounded.x1, "x2": bounded.x2,
                                          "y1": bounded.y2 + 1}))

        if cuboid.z1 < bounded.z1:
            result.add(cuboidRef(cuboid, {"x1": bounded.x1, "x2": bounded.x2,
                                          "y1": bounded.y1, "y2": bounded.y2,
                                          "z2": bounded.z1 - 1}))
        if bounded.z2 < cuboid.z2:
            result.add(cuboidRef(cuboid, {"x1": bounded.x1, "x2": bounded.x2,
                                          "y1": bounded.y1, "y2": bounded.y2,
                                          "z1": bounded.z2 + 1}))
        return result


def getInstructions():
    with open("Day 22 Input.txt") as data:
        dataList = list(data)
        dataList.reverse()
        for line in dataList:
            on = line[:2] == "on"
            cuboid = line[4-on:].strip().split(",")
            coords = []
            for c in cuboid:
                start, end = c.split("..")
                coords.extend((int(start[2:]), int(end)))
            yield Cuboid(on, *coords)


def main():
    cuboids = set()
    for cuboid in getInstructions():
        if len(cuboids) > 10000:
            print("nope")
            break
        fragments = {cuboid}
        for c in cuboids:
            cuts = set()
            for f in fragments:
                cuts.update(cutCuboid(c, f))
            fragments = cuts
        cuboids.update(fragments)
    print(f"Cuboids: {len(cuboids)}\nLights: {sum(countLights(c) for c in cuboids)}")


if __name__ == "__main__":
    main()
