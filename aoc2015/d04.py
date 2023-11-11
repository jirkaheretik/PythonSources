import hashlib

def readFile(filename):
    f = open(filename, "r")
    return f.read()

def processValues1(load):
    num = 1
    while True:
        meh = load + str(num)
        md5 = hashlib.md5(meh.encode()).hexdigest()
        if md5[:5] == "00000":
            print(f"{num} gives a hash {md5}")
            break
        num += 1
    return num

def processValues2(load, start):
    num = start
    while True:
        meh = load + str(num)
        md5 = hashlib.md5(meh.encode()).hexdigest()
        if md5[:6] == "000000":
            print(f"{num} gives a hash {md5}")
            break
        num += 1
    return num


if __name__ == "__main__":
    myKey = "yzbqklnj"
    result1 = processValues1(myKey)
    result2 = processValues2(myKey, result1)
    print("First adventcoin: {}".format(result1))
    print("Deeper adventcoin: {}".format(result2))
