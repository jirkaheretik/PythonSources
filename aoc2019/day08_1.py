"""
Processes chunk of data (string) and returns count of zeroes and product of number of ones and twos
"""
def countLayer(data):
    counts = [0, 0, 0]
    for i in range(len(data)):
        val = int(data[i])
        counts[val] += 1
    return (counts[0], counts[1] * counts[2])

def processData(values):
    IMGW = 25
    IMGH = 6
    imgSize = IMGW * IMGH
    minZeros = imgSize + 1  # init
    ourSum = 0

    pos = 0
    while pos < len(values):
        layer = values[pos:(pos+imgSize)]
        if len(layer) < imgSize:
            print("Data processed, expected result: {}".format(ourSum))
            return

        (zeros, sum) = countLayer(layer)
        print("Processed layer of length {} with {} zeros and result {}".format(len(layer), zeros, sum))
        if zeros < minZeros:
            minZeros = zeros
            ourSum = sum
        pos += imgSize


def readFile(filename):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
    return contents


if __name__ == "__main__":
    processData(readFile("d08input.txt"))
