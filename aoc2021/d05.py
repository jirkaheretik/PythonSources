from pprint import pprint

"""
                [B] [L]     [J]    
            [B] [Q] [R]     [D] [T]
            [G] [H] [H] [M] [N] [F]
        [J] [N] [D] [F] [J] [H] [B]
    [Q] [F] [W] [S] [V] [N] [F] [N]
[W] [N] [H] [M] [L] [B] [R] [T] [Q]
[L] [T] [C] [R] [R] [J] [W] [Z] [L]
[S] [J] [S] [T] [T] [M] [D] [B] [H]
 1   2   3   4   5   6   7   8   9 
"""
crates = []

def initCrates(crates):
    # crates = []
    crates.append(None)
    crates.append(["S", "L", "V"])
    crates.append(["J", "T", "N", "Q"])
    crates.append(["S", "C", "H", "F", "J"])
    crates.append(["T", "R", "M", "W", "N", "G", "B"])
    crates.append(["T", "R", "L", "S", "D", "H", "Q", "B"]) 
    crates.append(["M", "J", "B", "V", "F", "H", "R", "L"])
    crates.append(["D", "W", "R", "N", "J", "M" ]) 
    crates.append(["B", "Z", "T", "F", "H", "N", "D", "J" ]) 
    crates.append(["H", "L", "Q", "N", "B", "F", "T"])
    pprint(crates)

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
def readTopCrates(crates):
    result = ""
    for i in range(1, 10):
        result += crates[i][-1]
    return result   
    
def processValues1(load):
    score = 0
    initCrates(crates)
    pprint(crates)
    for line in load:
        countC = int(line[5:line.index(" ", 6)])
        posFrom = line.index("from ")
        fromC = int(line[posFrom + 5:line.index(" ", posFrom + 6)])
        posTo = line.index("to ")
        toC = int(line[posTo + 3:])
        # sanity check:
        constructedLine = f"move {countC} from {fromC} to {toC}"
        if constructedLine != line:
            print(f"Sum-tin-Wong: input '{line}' seems not to match output {constructedLine}")
            continue
        print(line)  
          
        # countC - number of steps
        # fromC - column from where to move the crates
        # toC - column to move crates to
        for i in range(countC):
            val = crates[fromC].pop()
            crates[toC].append(val)        
    return readTopCrates(crates)

def processValues2(load):
    score = 0
    initCrates(crates)
    for line in load:
        countC = int(line[5:line.index(" ", 6)])
        posFrom = line.index("from ")
        fromC = int(line[posFrom + 5:line.index(" ", posFrom + 6)])
        posTo = line.index("to ")
        toC = int(line[posTo + 3:])
        # sanity check:
        constructedLine = f"move {countC} from {fromC} to {toC}"
        if constructedLine != line:
            print(f"Sum-tin-Wong: input '{line}' seems not to match output {constructedLine}")
            continue
        #print(line)  
        # countC - number of steps
        # fromC - column from where to move the crates
        # toC - column to move crates to
        toMove = []
        for i in range(countC):
            toMove.append(crates[fromC].pop())
        while toMove:
            crates[toC].append(toMove.pop())        
    return readTopCrates(crates)

if __name__ == "__main__":
    myValues = readFile("d05_2.txt")
    # due to popping cannot call both processes in one go
    result1 = processValues1(myValues)
    crates = []                                        
    result2 = processValues2(myValues)
    print("Top crates: {}".format(result1))
    print("Top crates round 2: {}".format(result2))

