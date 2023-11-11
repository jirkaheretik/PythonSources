def readFile(filename):
    inputValues = list()
    f = open(filename, "r")
    if f.mode == "r":
        values = f.read().split(',')
        for x in values:
            print("Adding {} from input.".format(x))
            inputValues.append(int(x))
    return inputValues

def isPositional(mode, pos):
    tmp = mode
    while pos > 0:
        tmp = tmp // 10
        pos -= 1
    return (tmp % 10) == 0

def getMode(mode, pos):
    tmp = mode
    while pos > 0:
        tmp = tmp // 10
        pos -= 1
    return tmp % 10

def initValues(values, max):
    while len(values) < max:
        values.append(0)

def getAddress(values, relBase, start, pos, mode):
    m = getMode(mode, pos - 1)
    result = None
    if m == 0:  # positional
        result = values[start + pos]
    elif m == 1:  # immediate
        result = start + pos
    elif m == 2:  # relative
        result = relBase + values[start + pos]
    else:
        print("ERR: Unknown mode {} found at {}".format(m, start))
    return result

def getValue(values, relBase, start, pos, mode):
    return values[getAddress(values, relBase, start, pos, mode)]

def writeValue(values, relBase, start, pos, mode, value):
    values[getAddress(values, relBase, start, pos, mode)] = value

def processValues(values, start, input1, input2):
    inputUsed = False
    myOutput = None
    relBase = 0
    while True:
        try:
            instruction = values[start] % 100
            mode = values[start] // 100
            if instruction == 1:  # ADDITION
                writeValue(values, relBase, start, 3, mode, getValue(values, relBase, start, 1, mode) + getValue(values, relBase, start, 2, mode))
                start += 4
            elif instruction == 2:  # MULTIPLY
                writeValue(values, relBase, start, 3, mode, getValue(values, relBase, start, 1, mode) * getValue(values, relBase, start, 2, mode))
                start += 4
            elif instruction == 3:  # INPUT
                #print("Asking for input, using value 5")
                writeValue(values, relBase, start, 1, mode, input2 if inputUsed else input1)
                start += 2
                inputUsed = True
            elif instruction == 4: # OUTPUT
                outVal = getValue(values, relBase, start, 1, mode)
                myOutput = outVal
                print("Outputting value {} from instruction address {}".format(outVal, start))
                start += 2
            elif instruction == 5: # JUMP IF NONZERO
                start = getValue(values, relBase, start, 2, mode) if getValue(values, relBase, start, 1, mode) != 0 else start + 3
            elif instruction == 6: # JUMP IF ZERO
                start = getValue(values, relBase, start, 2, mode) if getValue(values, relBase, start, 1, mode) == 0 else start + 3
            elif instruction == 7: # IS LESS THAN
                writeValue(values, relBase, start, 3, mode, 1 if getValue(values, relBase, start, 1, mode) < getValue(values, relBase, start, 2, mode) else 0)
                start += 4
            elif instruction == 8: # IS EQUAL
                writeValue(values, relBase, start, 3, mode, 1 if getValue(values, relBase, start, 1, mode) == getValue(values, relBase, start, 2, mode) else 0)
                start += 4
            elif instruction == 9: # CHANGE REL BASE
                #idx = relBase +
                relBase = relBase + getValue(values, relBase, start, 1, mode)
                #print("Changing relBase to {}".format(relBase))
                start += 2
            elif instruction == 99: # PRG END
                print("FINISH Instruction at address {}".format(start))
                return myOutput
        except KeyError:
            print("Attempt to read unknown address {}, exitting.".format(start))
            return myOutput

if __name__ == "__main__":
    myValues = readFile("d09input.txt")
    initValues(myValues, 10000)
    processValues(myValues, 0, 2, 9999)
