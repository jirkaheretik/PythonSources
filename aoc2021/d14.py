
def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    score = 0
    minX = maxX = 500
    minY = maxY = 30
    for line in load:
        points = line.split(" -> ")
        for pt in points:
            x, y = pt.split(",")
            x = int(x)
            y = int(y)
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y
    print(f"Processed all lines, X is <{minX}, {maxX}>, Y is <{minY}, {maxY}>")            
    return score

def processValues2(load):
    score = 0
    return score

if __name__ == "__main__":
    myValues = readFile("d14.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Num of fully contained: {}".format(result1))
    print("Overlapping: {}".format(1000 - result2))

