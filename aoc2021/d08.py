from pprint import pprint

SIZE = 99

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
def processValues1(load, trees):
    score = 0
    # for all four directions:
    # west:
    for i in range(SIZE):
        lMax = -1
        for j in range(SIZE):
            val = int(load[i][j])
            if val > lMax:
                trees[i][j] = True
                lMax = val
            if val == 9:
                break # no more visible trees from this side
        # east
        lMax = -1
        for j in range(SIZE):
            val = int(load[i][SIZE - j - 1])
            if val > lMax:
                trees[i][SIZE - j - 1] = True
                lMax = val
            if val == 9:
                break # no more visible trees from this side
        
    # north:
    for j in range(SIZE):
        lMax = -1
        for i in range(SIZE):
            val = int(load[i][j])
            if val > lMax:
                trees[i][j] = True
                lMax = val
            if val == 9:
                break # no more visible trees from this side
        # south
        lMax = -1
        for i in range(SIZE):
            val = int(load[SIZE - i - 1][j])
            if val > lMax:
                trees[SIZE - i - 1][j] = True
                lMax = val
            if val == 9:
                break # no more visible trees from this side
        
    # count trees:
    for i in range(SIZE):
        for j in range(SIZE):
            if trees[i][j]:
                score += 1
            
    return score
    
def findCount(load, value, x, y, dX, dY):
    count = 0
    while (True):
        count += 1
        x += dX
        y += dY
        newVal = int(load[x][y])
        if newVal >= value or x == 0 or y == 0 or x == SIZE - 1 or y == SIZE - 1:
            break
    return count 
        

def processValues2(load, trees):
    score = 0 # max scenic score
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            # do not consider edges at all, since they have scenic score 0 
            # as there are 0 trees in of the directions
            val = int(load[i][j])
            scenicScore = findCount(load, val, i, j, 1, 0) * findCount(load, val, i, j, -1, 0) * findCount(load, val, i, j, 0, 1) * findCount(load, val, i, j, 0, -1)
            if scenicScore > score:
                print(f"New max is {scenicScore} over {score}")
                score = scenicScore
    return score

if __name__ == "__main__":
    myTrees = [[False for x in range(SIZE)] for x in range(SIZE)]
    myValues = readFile("d08.txt")
    result1 = processValues1(myValues, myTrees)
    result2 = processValues2(myValues, myTrees)
    print("Visible trees: {}".format(result1))
    print("Best scenic score is {}".format(result2))

