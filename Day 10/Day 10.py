code = [line.strip() for line in open("Day 10 Input.txt")]
flip = {")": "(", "]": "[", "}": "{", ">": "<"}
error = {")": 3, "]": 57, "}": 1197, ">": 25137}
endScore = {"(": 1, "[": 2, "{": 3, "<": 4}

corrupt = []
endings = []
for line in code:
    chunks = []
    for c in line:
        if c in "([{<":
            chunks.append(c)
        else:
            if chunks[-1] == flip[c]:
                chunks.pop()
            else:
                corrupt.append(c)
                break
    else:
        chunks.reverse()
        endings.append(chunks)

total = sum([error[c] for c in corrupt])
print("Total Error: " + str(total))

scores = [sum([endScore[c]*(5**(len(end) - i - 1)) for i, c in enumerate(end)]) for end in endings]    # lmao i one-lined it
scores.sort()
mid = scores[len(scores)//2]
print("End Score: " + str(mid))
