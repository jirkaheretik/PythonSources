from collections import Counter

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    return f.read()

"""
( - up one floor
) - down one floor
0 - start
where does it end?
"""
def processValues1(load):
    res = Counter(load)
    return res["("] - res[")"]

"""
( - up one floor
) - down one floor
0 - start
when (at what position) we first enter floor -1?
"""
def processValues2(load):
    counter = 0
    floor = 0
    for ch in load:
        counter += 1
        if ch == "(":
            floor += 1
        if ch == ")":
            floor -= 1
            if floor == -1:
                return counter
    



if __name__ == "__main__":
    myValues = readFile("d01.txt")
    print(f"End floor: {processValues1(myValues)}")
    print(f"Entering basement at instruction {processValues2(myValues)}")
