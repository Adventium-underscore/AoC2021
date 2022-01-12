from dataclasses import dataclass, field
import math


@dataclass
class Beacon:
    x: int
    y: int
    z: int
    distances: list = field(default_factory=list)

    def point(self):
        return self.x, self.y, self.z


def distance(b1, b2):
    return math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2 + (b2.z - b1.z)**2)


def scannerPrint(scanners, includeDistancs=False):
    for i, scanner in enumerate(scanners):
        print(f"--- Scanner {i} ---")
        for beacon in scanner:
            print(f"{beacon.x},{beacon.y},{beacon.z}")
            if includeDistancs:
                print("Distances: ")
                print(*beacon.distances, sep="\n")
                print()
        print()


def closeMatch(b1, b2):
    d1 = b1.distances
    d2 = b2.distances
    score = 0
    for d in d1:
        if d in d2:
            score += 1
    return score > len(d1) // 4


def calcDistances(scanners):
    for beacons in scanners:
        for beacon in beacons:
            distlist = []
            for b in beacons:
                if b != beacon:
                    distlist.append(distance(beacon, b))
            beacon.distances = distlist
    return scanners


def locateScanner(scanner, matches):
    (b1, s1), (b2, s2) = matches[0:2]
    db = [b2.x - b1.x, b2.y - b1.y, b2.z - b1.z]
    ds = [s2.x - s1.x, s2.y - s1.y, s2.z - s1.z]
    indexes = []
    for a in db:
        if a in ds:
            indexes.append((ds.index(a), 1))
        else:
            indexes.append((ds.index(-a), -1))
    location = [b1.point()[i] - s1.point()[n] * s for i, (n, s) in enumerate(indexes)]

    newScanner = []
    for beacon in scanner:
        newPoint = [location[i] + beacon.point()[n] * s for i, (n, s) in enumerate(indexes)]
        newScanner.append(Beacon(*newPoint, distances=beacon.distances))
    return location, newScanner


def main():
    scanners = []
    with open("Day 19 Input.txt") as data:
        while data.readline():
            beacons = []
            point = data.readline().strip()
            while point:
                x, y, z = point.split(",")
                beacons.append(Beacon(int(x), int(y), int(z)))
                point = data.readline().strip()
            scanners.append(beacons)

    scanners = calcDistances(scanners)
    locations = [[0, 0, 0]]
    while len(scanners) > 1:
        scanner = scanners[0]
        for i, s in enumerate(scanners[1:]):
            i += 1
            matches = []
            for beacon in scanner:
                for b in s:
                    if closeMatch(beacon, b):
                        matches.append((beacon, b))
            if matches:
                print(f"Match: Scanner {i}/{len(scanners) - 1} with {len(matches)}")
                location, scanUpdate = locateScanner(s, matches)
                locations.append(location)
                for beacon in scanUpdate:
                    duplicate = False
                    for b in scanner:
                        if beacon.point() == b.point():
                            duplicate = True
                            break
                    if not duplicate:
                        scanner.append(beacon)
                scanners.pop(i)
                break

    print()
    print(f"Total beacons: {len(scanners[0])}")
    manhattan = 0
    for l1 in locations:
        for l2 in locations:
            manhattan = max(sum(b-a for a, b in zip(l1, l2)), manhattan)
    print(f"Largest Manhattan: {manhattan}")


if __name__ == "__main__":
    main()
