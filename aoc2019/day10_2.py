import math
from math import atan2,pi,degrees

def readFile(filename):
    inputValues = list()
    f = open(filename, "r")
    if f.mode == "r":
        values = f.readlines()
        for line in values:
            inputValues.append(list(line.strip()))
    return inputValues

def isAsteroid(values, row, col):
    return values[row][col] == "#"

def countAsteroids(values):
    sum = 0
    for r in values:
        for c in r:
            if c == "#":
                sum += 1
    return sum

def angle(xdiff,ydiff):
    return round(degrees((atan2(xdiff,ydiff) + 2 * pi) % (2 * pi)), 5)

def processValues(values):
    print("Having field of {}x{}".format(len(values[0]), len(values)))
    for row in values:
        line = ""
        for col in row:
            line += col
        print(line)

def countVisibleAsteroidsFromPos(values, row, col):
    # if I am not an asteroid, do not see anything...
    if not isAsteroid(values, row, col):
        return 0
    angles = set()
    for r in range(MAXY):
        for c in range(MAXX):
            if row == r and col == c:
                continue
            if not isAsteroid(values, r, c):
                continue
            angles.add(angle(r - row, c - col))
    return len(angles)

def isVisibleFrom(values, row, col, r, c):
    # 1. najit spolecny delitel rozdilu souradnic
    (dX, dY) = findSmallestStep(col - c, row - r)
    #print("DBG step {}, {}".format(dY, dX))
    # 2. krokovat, a hledat jestli je tam asteroid
    posX = c + dX
    posY = r + dY
    while (posX != col or posY != row) and posX >= 0 and posX <= MAXX and posY >= 0 and posY<= MAXY:
        if isAsteroid(values, posY, posX):
            #print("Found asteroid at [{}, {}]".format(posX, posY))
            return False
        posX += dX
        posY += dY
    # TEMPORARY:
    return True

def countAzimuthAndDistanceFromPos(values, row, col):
    if not isAsteroid(values, row, col):
        return None
    result = set()
    for r in range(MAXY):
        for c in range(MAXX):
            if row == r and col == c:
                continue
            if not isAsteroid(values, r, c):
                continue
            result.add((angle(r - row, c - col), abs(r - row) + abs(c - col)))
    return result


def findSmallestStep(a, b):
    if a == 0:
        return 0, b/abs(b)
    if b == 0:
        return a/abs(a), 0
    if abs(a) == abs(b):
        return a/abs(a), b/abs(b)
    if isPrime(abs(a)) or isPrime(abs(b)):
        return a, b
    for i in range(12, 1, -1):
        if a % i == 0 and b % i == 0:
            return a/i, b/i
    #TEMPORARY
    return a, b

def isPrime(number):
    if number == 1:
        return False
    if number < 4:
        return True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    myValues = readFile("d10input.txt")
    processValues(myValues)
    MAXX = len(myValues[0])
    MAXY = len(myValues)

    statX = -1
    statY = -1


    maxAsteroids = 0
    for x in range(MAXX):
        for y in range(MAXY):
            pocet = countVisibleAsteroidsFromPos(myValues, y, x)
            if pocet > maxAsteroids:
                print("Found new maximum {} at [{}, {}]".format(pocet, y, x))
                maxAsteroids = pocet
                statX = x
                statY = y
    print("Maximum is {}, radar (and laser) will be at [{}, {}]".format(maxAsteroids, statX, statY))

    for (ang, dist) in countAzimuthAndDistanceFromPos(myValues, y, x):
        print("{};{}".format(ang, dist))

    #And now do the destruction...


    #print("Asteroids visible from [2, 1]: {}".format(countVisibleAsteroidsFromPos(myValues, 1, 2)))


    """
    print("Total number of asteroids here: {}".format(countAsteroids(myValues)))
    print("Is at [1,5]? {}".format(isAsteroid(myValues, 1, 5)))
    print("Is at [5,1]? {}".format(isAsteroid(myValues, 5, 1)))
    print("Asteroids from [1, 1]: {}".format(countVisibleAsteroidsFromPos(myValues, 1, 1)))
    print("Asteroids visible from [1, 2]: {}".format(countVisibleAsteroidsFromPos(myValues, 1, 2)))

    values = [2, 4, 1, 7, 9, 12, 26, 8, 13]
    for i in values:
        print("Is {} prime? {}".format(i, isPrime(i)))

    values = [13, -7, 8, -8, 4, -12, -15, 25, 12, 3, 0, 8, 23]
    for i in range(0, len(values)-1):
        print("[{}, {}] with result: {}".format(values[i], values[i+1], findSmallestStep(values[i], values[i+1])))
    """
