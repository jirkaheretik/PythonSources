def readFile(filename):
    line1 = list()
    line2 = list()
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.readlines()
        line1 = contents[0].split(',')
        line2 = contents[1].split(',')
    return (line1, line2)

def processHand(myList):
    x = 0
    y = 0
    xList = list()
    yList = list()
    for val in myList:
        dir = val[0]
        intVal = int(val[1:].strip())
        if dir == "R":
            xList.append((x, y, x + intVal, y))
            x += intVal
        elif dir == "L":
            xList.append((x - intVal, y, x, y))
            x -= intVal
        elif dir == "U":
            yList.append((x, y, x, y + intVal))
            y += intVal
        elif dir == "D":
            yList.append((x, y - intVal, x, y))
            y -= intVal
        else:
            print("Found wrong instruction {}".format(dir))
    print("List processed with end at [{}, {}]".format(x, y))
    return (xList, yList)

def findClosestIntersection(line, listOfLines):
    MIN = 10000
    for (x1, y1, x2, y2) in listOfLines:
        (nx1, ny1, nx2, ny2) = line
        if nx1 == nx2:  #line is vertical
            if y1 != y2:
                print("Paralel lines found?! Line1 [{}, {}, {}, {}], Line2 [{}, {}, {}, {}]".format(nx1, ny1, nx2, ny2, x1, y1, x2, y2))
            elif ny1 <= y1 and ny2 >= y1 and x1 <= nx1 and x2 >= nx1:
                print("Found intersection at [{}, {}]".format(nx1, y1))
                if nx1 != 0 and y1 != 0:
                    MIN = min(MIN, abs(nx1) + abs(y1))
        elif ny1 == ny2:  #line is horizontal
            if x1 != x2:
                print("Paralel lines found?! Line1 [{}, {}, {}, {}], Line2 [{}, {}, {}, {}]".format(nx1, ny1, nx2, ny2, x1, y1, x2, y2))
            elif y1 <= ny1 and y2 >= ny1 and nx1 <= x1 and nx2 >= x1:
                print("Found intersection at [{}, {}]".format(x1, ny1))
                if x1 != 0 and ny1 != 0:
                    MIN = min(MIN, abs(x1) + abs(ny1))
    return MIN

if __name__ == "__main__":
    MIN = 10000
    (left, right) = readFile("d03input.txt")
    #print("Left: {}".format(left))
    #print("Right: {}".format(right))
    (x1List, y1List) = processHand(left)
    (x2List, y2List) = processHand(right)

    for line in x2List:
        MIN = min(MIN, findClosestIntersection(line, y1List))
    for line in y2List:
        MIN = min(MIN, findClosestIntersection(line, x1List))

    print("Closest intersection is {}".format(MIN))
