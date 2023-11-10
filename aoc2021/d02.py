MY = ["*", "X", "Y", "Z"]
OP = ["C", "A", "B", "C", "A"]

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    score = 0
    # cycle all rounds
    for round in load:
        if not round:
            break
        op = round[0] 
        my = round[2]
        # find my column:
        myNum = MY.index(my)
        # score
        if OP[myNum - 1] == op:
            # win
            score += 6
        elif OP[myNum] == op:
            # draw
            score += 3
        score += myNum 
         
    return score

def processValues2(load):
    score = 0
    OP[0] = "*"
    # cycle all rounds
    for round in load:
        if not round:
            break
        op = round[0] 
        res = round[2]
        # find ops column:
        hisNum = OP.index(op)
        # score
        if res == "Z":
            # win
            score += 6
            score += 1 if hisNum == 3 else hisNum + 1
        elif res == "Y":
            # draw
            score += 3 + hisNum
        else:
            # loss
            score += 3 if hisNum == 1 else hisNum - 1
        # score += myNum 
         
    return score


if __name__ == "__main__":
    myValues = readFile("d02.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("My score 1st way: {}".format(result1))
    print("My score correct way: {}".format(result2))
