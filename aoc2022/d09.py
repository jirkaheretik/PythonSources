from pprint import pprint
# from numpy import sign


def sg(x):
    return (x > 0) - (x < 0)

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
def wiggle(x1, y1, x2, y2):
    """
    compares those two points and return a tuple 
    with directions to move the second part to 
    tail the first - that is (x, y) where x, y in (-1, 0, 1)
    """    
    # adjust tail if needed:
    dx = dy = 0
    if (abs(x2 - x1) > 1) or (abs(y2 - y1) > 1):
        # adjust possibly both coordinates:
        dx = sg(x1 - x2)
        dy = sg(y1 - y2)
    return (dx, dy)
    

def processValues1(load):
    score = 0
    tailPositions = set()
    tailPositions.add((0, 0))
    xt = yt = xh = yh = 0 # starting positions
    for instruction in load:
        direction, steps = instruction.split(" ")
        steps = int(steps)
        dx = dy = 0
        if direction == "D":
            dy = -1
        elif direction == "U":
            dy = 1
        elif direction == "R":
            dx = 1
        elif direction == "L":
            dx = -1
        else:
            print(f"Unknown instruction {direction}")
            continue
        for i in range(steps):
            # do a step with tail:
            xh += dx
            yh += dy

            """
            # adjust tail if needed:
            if (abs(xt - xh) > 1) or (abs(yt - yh) > 1):
                # adjust possibly both coordinates:
                dx1 = sg(xh - xt)
                dy1 = sg(yh - yt)
                dx2, dy2 = wiggle(xh, yh, xt, yt)  
                if dx1 != dx2 or dy1 != dy2:
                    print(f"Fail, correct is ({dx1},{dy1}), but wiggle returns ({dx2},{dy2})")
                
                xt += sg(xh - xt)
                yt += sg(yh - yt)
                # sanity check:
                if (abs(xt - xh) > 1) or (abs(yt - yh) > 1):
                    print(f"Positional fail while dragging the tail, instruction '{direction} {steps}' step {i}, head ({xh}, {yh}), tail ({xt}, {yt})")
            else:
                ddx, ddy = wiggle(xh, yh, xt, yt)
                if ddx != 0 or ddy != 0:
                    print(f"Fail. Head ({xh},{yh}), Tail ({xt},{yt}) and wiggle returned ({ddx},{ddy})")
            """
            ddx, ddy = wiggle(xh, yh, xt, yt)
            xt += ddx
            yt += ddy
            #"""
            # add new tail position to the set
            tailPositions.add((xt, yt)) 
    return len(tailPositions)
    
def processValues2(load):
    score = 0
    tailPositions = set()
    tailPositions.add((0, 0))
    # starting positions
    snake = [[0 for x in range(2)] for x in range(10)]
    
    for instruction in load:
        direction, steps = instruction.split(" ")
        steps = int(steps)
        dx = dy = 0
        if direction == "D":
            dy = -1
        elif direction == "U":
            dy = 1
        elif direction == "R":
            dx = 1
        elif direction == "L":
            dx = -1
        else:
            print(f"Unknown instruction {direction}")
            continue
        for i in range(steps):
            # do a step with head:
            snake[0][0] += dx
            snake[0][1] += dy
            # now process the tail:
            for i in range(1, 10):
                ddx, ddy = wiggle(snake[i-1][0], snake[i-1][1], snake[i][0], snake[i][1])
                snake[i][0] += ddx
                snake[i][1] += ddy
            # add new tail position to the set
            tailPositions.add((snake[9][0], snake[9][1])) 
    return len(tailPositions)

if __name__ == "__main__":
    myValues = readFile("d09.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Tail positions: {}".format(result1))
    print("Long tail positions {}".format(result2))

