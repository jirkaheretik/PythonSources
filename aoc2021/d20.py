import math 

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(int(x.strip()))
    return inputValues
    
def processValues1(vstup):
    score = 0
    load = vstup.copy()
    count = len(load)
    
    # "handle" dupes
    for i in range(len(load)):
        val = load[i]
        while val in load and load.index(val) < i:
            val += 0.1
        load[i] = val
    
    iteration = tuple(load) # copy of the list, original order
    for num in iteration:
        idx = load.index(num)
        del load[idx]
        #newPos = idx + num % count
        newPos = (idx + math.floor(num)) % (count - 1)
        load.insert(newPos, num)
        # dbg for test input:
        if count < 1000:
            print(f"{load} idx: {idx}, num: {num}, count: {count}, newPos: {newPos}")
    # sum of 1000th, 2000th and 3000th position after zero:
    idx = load.index(0)
    #print(load)
    print(f"load[{idx}]=0, count = {count}")
    for i in range(3):
        idx = (idx + 1000) % count
        print(f"load[{idx}]={load[idx]}")
        try:
            score += math.floor(load[idx])
        except Exception:
            print(f"DBG i: {i}, idx: {idx}, count: {count}, pole: {load}")
    return score
    
def processValues2(load):
    score = 0
    count = len(load)
    
    # multiply by key and handle dupes
    for i in range(len(load)):
        val = load[i] * 811589153
        while val in load and load.index(val) < i:
            val += 0.1
        load[i] = val
    
    iteration = tuple(load) # copy of the list, original order
    for _ in range(10):
      for num in iteration:
          idx = load.index(num)
          del load[idx]
          #newPos = idx + num % count
          newPos = (idx + math.floor(num)) % (count - 1)
          load.insert(newPos, num)
          # dbg for test input:
          if count < 1000:
              print(f"{load} idx: {idx}, num: {num}, count: {count}, newPos: {newPos}")
    # sum of 1000th, 2000th and 3000th position after zero:
    idx = load.index(0)
    #print(load)
    print(f"load[{idx}]=0, count = {count}")
    for i in range(3):
        idx = (idx + 1000) % count
        print(f"load[{idx}]={load[idx]}")
        try:
            score += math.floor(load[idx])
        except Exception:
            print(f"DBG i: {i}, idx: {idx}, count: {count}, pole: {load}")
    return score

if __name__ == "__main__":
    myValues = readFile("d20.txt")
    testValues = [1, 2, -3, 3, -2, 0, 4]
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Sum of three after mixing: {}".format(result1))
    print("New sum after 10x mixing: {}".format(result2))

# Failed answers P1: -1891, 654 too low, 
# 