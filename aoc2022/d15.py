
def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1 - y2)
    
def getCoords(subst):
    left, right = subst.split(", y=")
    return int(left), int(right)

def processValues1(load):
    score = 0
    sensors = []
    constraints = []
    for line in load:
        record = dict()
        mid = line.index(": closest beacon")
        xs, ys = getCoords(line[12:mid])
        xb, yb = getCoords(line[mid+25:])
        record["x"] = xs
        record["y"] = ys
        record["bx"] = xb
        record["by"] = yb
        record["mh"] = manhattan(xs, ys, xb, yb)
        #outlier = manhattan(xs, ys, 2159715, 2000000)
        #print(f"Sensor {xs},{ys} with beacon {record['mh']} is {outlier} away from the weird spot.") 
        sensors.append(record)
        #find lowX-highX where cannot be a beacon:
        dist = record["mh"] - abs(ys - 2000000)
        if dist >= 0:
            #print(f"No beacons between {xs-dist} and {xs+dist}")
            #print(f"{xs-dist};{xs+dist}")
            """
            PART 1 Solution here: the problem is there is ONE beacon 
            on the line y = 2M, and we need to lower the result by this one.
            """
            constraints.append((xs - dist, xs + dist))
    """        
    for i in range(-3000000,7000000):
        for s in sensors:
            dist = manhattan(i, 2000000, s["x"], s["y"])
            if dist <= s["mh"]:
                # no beacon here, otherwise lock elsewhere       
                score += 1
                #print(f"No beacon at {i},2M, as its distance to sensor at {s['x']},{s['y']} is {dist} which is smaller than {s['mh']}")
                break
        
        # print(f"Sensor {sensor}, beacon {beacon}")
    """    
    return score
    
def checkLargerSensors(sensors, index, xpos, ypos):
    for i in range(index, len(sensors)):
        if manhattan(xpos, ypos, sensors[i]["x"], sensors[i]["y"]) <= sensors[i]["mh"]:
            return False
    print(f"Found something at {xpos}, {ypos}")
    return True
    
def checkRangeAndPos(x, y, sensors, index):
    if x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000:
        checkLargerSensors(sensors, index, x, y)
    
def testPos(xpos, ypos, sensors):
    for s in sensors:
        diff = manhattan(xpos, ypos, s["x"], s["y"]) 
        if diff > s["mh"]:
            print(f"All ok against sensor {s['x']}/{s['y']} by {diff-s['mh']}")
        else:
            print(f"Failed against sensor {s['x']}/{s['y']}")                          

def processValues2(load):
    score = 0
    sensors = []
    for line in load:
        record = dict()
        mid = line.index(": closest beacon")
        xs, ys = getCoords(line[12:mid])
        xb, yb = getCoords(line[mid+25:])
        record["x"] = xs
        record["y"] = ys
        record["bx"] = xb
        record["by"] = yb
        record["mh"] = manhattan(xs, ys, xb, yb)
        sensors.append(record)
    sortedSensors = sorted(sensors, key = lambda d: d['mh'])
    testPos(2614408, 2860779, sensors)
    print(f"Part 2 result: {2614408*4000000+2860779}")
    """
    for s in sortedSensors:
        # circle round its edges and check if any of the poins is farther away from all the other sensors than their beacon
        idx = sortedSensors.index(s)
        for x in range(s["mh"] + 1):
            y = s["mh"] + 1 - x 
            checkRangeAndPos(s["x"] - x, s["y"] - y, sortedSensors, idx)
            checkRangeAndPos(s["x"] - x, s["y"] + y, sortedSensors, idx)
            checkRangeAndPos(s["x"] + x, s["y"] - y, sortedSensors, idx)
            checkRangeAndPos(s["x"] + x, s["y"] + y, sortedSensors, idx)
                                 
        print(f"Done for sensor at {s['x']}/{s['y']}")
    """
    for first in range(len(sensors) - 1):
        for second in range(first + 1, len(sensors)):
            F = sensors[first]
            S = sensors[second]
            if manhattan(F["x"], F["y"], S["x"], S["y"]) == F["mh"] + S["mh"] + 2:
                print(f"BINGO! Sensor ({F['x']}, {F['y']}) with Beacon dist {F['mh']} and sensor ({S['x']}, {S['y']}) with beacon dist {S['mh']}")        
    
    return score

if __name__ == "__main__":
    myValues = readFile("d15.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("No beacons on line y=2M: {}".format(result1))
    print("Not implemented: {}".format(result2))

# Failed answers:
# 5508235 too high
# 5508000 too low