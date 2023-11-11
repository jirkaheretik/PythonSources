"""
Processes chunk of data (string) and returns count of zeroes and product of number of ones and twos
"""
def countLayer(data):
    counts = [0, 0, 0]
    for i in range(len(data)):
        val = int(data[i])
        counts[val] += 1
    return (counts[0], counts[1] * counts[2])

def mergeLayers(target, newlayer):
    for i in range(imgSize):
        if target[i] == "2" and newlayer[i] != "2":
            #print("replacing value with {}".format(newlayer[i]))
            target[i] = newlayer[i]
    return target

def processData(values):
    result = "222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"

    """
    result = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ]
    """

    pos = 0
    while pos < len(values):
        layer = values[pos:(pos+imgSize)]
        if len(layer) < imgSize:
            print("Data processed, result:")
            printLayer(result)
            return

        #print("New layer:")
        #printLayer(layer)
        result = mergeLayers(result, layer)
        print("Target layer:")
        printLayer(result)
        pos += imgSize

def printLayer(data):
    for r in range(IMGH):
        line = ""
        for c in range(IMGW):
            char = data[r * IMGW + c]
            if char == "0":
                line += " "
            elif char == "1":
                line += "*"
            else:
                 line += "."
        print(line)

def readFile(filename):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
    return contents

IMGW = 25
IMGH = 6
imgSize = IMGW * IMGH

if __name__ == "__main__":
    processData(readFile("d08input.txt"))
