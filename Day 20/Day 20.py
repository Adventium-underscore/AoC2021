def expand(image, c):
    blank = c * (len(image[0]) + 2)
    newImage = [blank]
    for row in image:
        newImage.append(c + row + c)
    newImage.append(blank)
    return newImage


def getNum(image, x, y):
    numString = ""
    for px, py in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]:
        numString += image[py][px:px+3]
    trans = numString.maketrans(".#", "01")
    return int(numString.translate(trans), 2)


def main():
    with open("Day 20 Input.txt") as data:
        enhance = next(data).strip()
        next(data)
        image = expand([line.strip() for line in data], ".")
        # print(*image, "\n", sep="\n")
        ends = enhance[0] + enhance[-1]
        c = ends[0] == "#"

        for i in range(50):
            image = expand(image, ends[c])
            c = "#" == ends[0] == ends[c]
            newImage = [ends[c] * len(image[0]) for _ in range(len(image))]
            for y, row in enumerate(image[1:-1]):
                y += 1
                newRow = ends[c]
                for x in range(len(row) - 2):
                    x += 1
                    num = getNum(image, x, y)
                    newRow += enhance[num]
                newImage[y] = newRow + ends[c]
            image = newImage
            # print(f"Iteration {i+1}:", *image, "\n", sep="\n")
        print("Total lights: " + str(sum(row.count("#") for row in image)))


if __name__ == "__main__":
    main()
