import hashlib

def readFile(filename):
    f = open(filename, "r")
    return f.read()
    
def step(input):
    num = ""
    count = 0
    result = ""
    for c in input:
        if c == num:
            # next occurence
            count += 1
        else:
            # new one
            if num:
                result += str(count) + num
            num = c
            count = 1
    result += str(count) + num
    return result

def processValues1(load, steps):
    for i in range(steps):
        # print(f"{i}. ({len(load)}) {load}")
        load = step(load)
    # print(f"{i}. ({len(load)}) {load}")
    return len(load)

def processValues2(load, start):
    return 0


if __name__ == "__main__":
    myKey = "1113122113"
    result1 = processValues1(myKey, 40)
    result2 = processValues1(myKey, 50)
    print("Length after step 40: {}".format(result1))
    print("Length after step 50: {}".format(result2))
