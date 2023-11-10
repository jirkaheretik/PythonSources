
def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    score = 0
    for line in load:
        if not line:
            break
        (left, right) = line.split(",")
        (e1low, e1hi) = left.split("-")
        (e2low, e2hi) = right.split("-")
        e1low = int(e1low)
        e1hi  = int(e1hi)
        e2low = int(e2low)
        e2hi  = int(e2hi)
        if (e1low <= e2low and e1hi >= e2hi) or (e2low <= e1low and e2hi >= e1hi):
            # fully contained
            print(f"Fully contained: ({e1low}-{e1hi}),({e2low}-{e2hi})")
            score += 1
        
    return score

def processValues2(load):
    score = 0
    for line in load:
        if not line:
            break
        (left, right) = line.split(",")
        (e1low, e1hi) = left.split("-")
        (e2low, e2hi) = right.split("-")
        e1low = int(e1low)
        e1hi  = int(e1hi)
        e2low = int(e2low)
        e2hi  = int(e2hi)
        if e1hi < e2low or e2hi < e1low:
            # non overlapping
            print(f"Non overlapping: ({e1low}-{e1hi}),({e2low}-{e2hi})")
            score += 1
    return score

if __name__ == "__main__":
    myValues = readFile("d04.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Num of fully contained: {}".format(result1))
    print("Overlapping: {}".format(1000 - result2))

