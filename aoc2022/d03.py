PRIORITIES = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getPrio(char):
    return PRIORITIES.index(char)

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    score = 0
    for sack in load:
        if not sack:
            break
        half = int(len(sack)/2)
        # print(f"Sack {sack} has length {len(sack)} and half is {half}")
        first = sack[:half]
        second = sack[half:]
        # print(f"Sack {sack} divided into {first} and {second}")
        if len(first) != len(second):
            # failed sanity check
            print(f"Sanity check failed for sack {sack}, first half '{first}', second half '{second}'")
            return 0
        for c in first:
            if c in second:
                # print(f"Found item {c} in both backpacks.")
                score += getPrio(c) 
                break
         
    return score

def findCommonCharsPrio(s1, s2, s3):
    for c in PRIORITIES:
        if c in s1 and c in s2 and c in s3:
            # print(f"{c} common for {s1}, {s2} and {s3}")
            return getPrio(c)
    print(f"Found no common for {s1}, {s2} and {s3}")
    return 0    


def processValues2(load):
    score = 0
    i = 0
    while i < len(load):
        score += findCommonCharsPrio(load[i], load[i+1], load[i+2])
        i += 3
        
    return score


if __name__ == "__main__":
    myValues = readFile("d03.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Sum of priorities: {}".format(result1))
    print("Sum of badges priorities: {}".format(result2))
