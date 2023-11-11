def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x)
    return inputValues

def processValues1(load):
    max = 0
    thisElf = 0
    for line in load:
        if line.strip():
            thisElf += int(line.strip())
        else:
            # compare
            if thisElf > max:
                print(f"New max {thisElf}\n")
                max = thisElf
            thisElf = 0
    return max

def processValues2(load):
    elves = []
    thisElf = 0
    for line in load:
        if line.strip():
            thisElf += int(line.strip())
        else:
            elves.append(thisElf)
            print(f"Adding elf with {thisElf} calories")
            thisElf = 0
    elves.sort(reverse=True)
    max = elves[0]+elves[1]+elves[2]
    return max


if __name__ == "__main__":
    myValues = readFile("d01.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Max calories: {}".format(result1))
    print("Sum of 3 max: {}".format(result2))
