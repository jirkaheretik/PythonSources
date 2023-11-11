def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    paper = 0
    ribbon = 0
    for line in load:
        if not line:
            break
        dimensions = line.split("x")
        for i in range(3):
            dimensions[i] = int(dimensions[i])
        dimensions.sort()
        (a, b, c) = tuple(dimensions)
        paper += 3*a*b + 2*a*c + 2*b*c
        ribbon += 2*a + 2*b + a*b*c
    return (paper, ribbon)


if __name__ == "__main__":
    myValues = readFile("d02.txt")
    (result1, result2) = processValues1(myValues)
    # result2 = processValues2(myValues)
    print("Wrapping paper needed: {} sq ft".format(result1))
    print("Ribbon needed: {} ft".format(result2))
