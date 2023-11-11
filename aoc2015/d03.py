def readFile(filename):
    f = open(filename, "r")
    return f.read()

def processValues1(load):
    count = 1
    x = 0
    y = 0
    visited = set()
    visited.add((0, 0))
    for c in load:
        if c == ">":
            y += 1
        if c == "<":
            y -= 1
        if c == "^":
            x += 1
        if c == "v":
            x -= 1
        visited.add((x, y))
        count += 1
    #print(f"Done {count} steps.")
    #print(visited)
    return len(visited)

def processValues2(load):
    count = 1
    xS = 0
    yS = 0
    xRS = 0
    yRS = 0
    visited = set()
    visited.add((0, 0))
    for c in load:
        if c == ">":
            if count % 2:
                yS += 1
            else:
                yRS += 1    
        if c == "<":
            if count % 2:
                yS -= 1
            else:
                yRS -= 1
        if c == "^":
            if count % 2:
                xS += 1
            else:
                xRS += 1
        if c == "v":
            if count % 2:
                xS -= 1
            else:
                xRS -= 1
        if count % 2:
            visited.add((xS, yS))
        else:
            visited.add((xRS, yRS))
        count += 1
    print(f"Done {count} steps.")
    print(visited)
    return len(visited)

if __name__ == "__main__":
    myValues = readFile("d03.txt")
    print(f"Velikost vstupu: {len(myValues)}")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Santa visited {} houses".format(result1))
    print("Santa or RoboSanta visited {} houses".format(result2))