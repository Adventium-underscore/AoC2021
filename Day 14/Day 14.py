from collections import defaultdict
polymer,_,*data = [line.strip() for line in open("Day 14 Input.txt")]
pairs = defaultdict(int)
for p in zip(polymer[:-1],polymer[1:]):
    pairs[p] += 1
rules = {(a,b):((a,o),(o,b)) for (a,b),o in [line.split(" -> ") for line in data]}

for step in range(40):
    newPairs = defaultdict(int)
    for i,o in rules.items():
        if i in pairs:
            for p in o:
                newPairs[p] += pairs[i]
    pairs = newPairs

counts = defaultdict(int)
for p,n in pairs.items():
    for c in p:
        counts[c] += n/2
counts[polymer[0]] += 0.5
counts[polymer[-1]] += 0.5
v = counts.values()
print(max(v) - min(v))
