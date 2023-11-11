
def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
myLights = [[False for x in range(1000)] for x in range(1000)]
    
def doBulb(action, i, j):
    if action == "X":
        myLights[i][j] = not myLights[i][j]
    else:
        # True for T, False for t
        myLights[i][j] = (action == "T")

def doBulb2(action, i, j):
    if action == "X":
        myLights[i][j] += 2
    elif action == "T":
        myLights[i][j] += 1
    else:
        if myLights[i][j] > 0:
            myLights[i][j] -= 1

def processValues1(load):
    print("Processing input 1")
    for line in load:
        (action, lower, upper) = line.split("-")
        (x1, y1) = lower.split(",")
        (x2, y2) = upper.split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if x1 > x2 or y1 > y2:
            print("Wrong coordinates, need to revisit!")
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                doBulb(action, i, j)
    print("Done input 1")
    on = 0
    for i in range(1000):
        for j in range(1000):
            if myLights[i][j]:
                on += 1              
    return on

def processValues2(load):
    print("Processing input 2")
    for line in load:
        (action, lower, upper) = line.split("-")
        (x1, y1) = lower.split(",")
        (x2, y2) = upper.split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if x1 > x2 or y1 > y2:
            print("Wrong coordinates, need to revisit!")
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                doBulb2(action, i, j)
    print("Done input 2")
    on = 0
    for i in range(1000):
        for j in range(1000):
            on += myLights[i][j]
    return on


if __name__ == "__main__":
    myValues = readFile("d06v2.txt")
    result1 = processValues1(myValues)
    myLights = [[0 for x in range(1000)] for x in range(1000)]
    result2 = processValues2(myValues)
    print("Lighted: {}".format(result1))
    print("Lights revisited: {}".format(result2))
