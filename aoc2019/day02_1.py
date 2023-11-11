def readFile(filename):
    inputValues = list()
    f = open(filename, "r")
    if f.mode == "r":
        values = f.read().split(',')
        for x in values:
            print("Adding {} from input.".format(x))
            inputValues.append(int(x))
    return inputValues

def processValues(values, start):
    while True:
        try:
            instruction = values[start]
            if instruction == 1:
                values[values[start + 3]] = values[values[start + 2]] + values[values[start + 1]]
                start += 4
            elif instruction == 2:
                values[values[start + 3]] = values[values[start + 2]] * values[values[start + 1]]
                start += 4
            elif instruction == 99:
                return
        except KeyError:
            print("Attempt to read unknow address {}, exitting.".format(start))
            return

def initialization(values):
    values[1] = 12
    values[2] = 2

if __name__ == "__main__":
    myValues = readFile("d02input.txt")
    initialization(myValues)
    processValues(myValues, 0)
    print("Value at position ZERO: {}".format(myValues[0]))
