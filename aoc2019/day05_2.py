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

def processValues(values, start):
    while True:
        try:
            instruction = values[start] % 100
            mode = values[start] // 100
            if instruction == 1:  # ADDITION
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                if not isPositional(mode, 2):
                    print("Error, trying to write to immediate value! Using positional anyway. At pos: {}, mode: {}".format(start, mode))
                values[values[start + 3]] = op1 + op2
                start += 4
            elif instruction == 2:  # MULTIPLY
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                if not isPositional(mode, 2):
                    print("Error, trying to write to immediate value! Using positional anyway. At pos: {}, mode: {}".format(start, mode))
                values[values[start + 3]] = op1 * op2
                start += 4
            elif instruction == 3:  # INPUT
                print("Asking for input, using value 5")
                if mode > 0:
                    print("WARN: Mode {} not compatible with instruction input, ignoring...".format(mode))
                values[values[start + 1]] = 5
                start += 2
            elif instruction == 4: # OUTPUT
                outVal = 0
                if mode > 0:
                    outVal = values[start + 1]
                else:
                    outVal = values[values[start + 1]]
                print("Outputting value {} from instruction address {}".format(outVal, start))
                start += 2
            elif instruction == 5: # JUMP IF NONZERO
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                start = op2 if op1 != 0 else start + 3
            elif instruction == 6: # JUMP IF ZERO
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                start = op2 if op1 == 0 else start + 3
            elif instruction == 7: # IS LESS THAN
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                if not isPositional(mode, 2):
                    print("Error, trying to write to immediate value! Using positional anyway. At pos: {}, mode: {}".format(start, mode))
                values[values[start + 3]] = 1 if op1 < op2 else 0
                start += 4
            elif instruction == 8: # IS EQUAL
                op1 = values[values[start + 1]] if isPositional(mode, 0) else values[start + 1]
                op2 = values[values[start + 2]] if isPositional(mode, 1) else values[start + 2]
                if not isPositional(mode, 2):
                    print("Error, trying to write to immediate value! Using positional anyway. At pos: {}, mode: {}".format(start, mode))
                values[values[start + 3]] = 1 if op1 == op2 else 0
                start += 4
            elif instruction == 99: # PRG END
                return
        except KeyError:
            print("Attempt to read unknown address {}, exitting.".format(start))
            return

def initialization(values):
    values[1] = 12
    values[2] = 2

if __name__ == "__main__":
    myValues = readFile("d05input.txt")
    #initialization(myValues)
    processValues(myValues, 0)
    print("Value at position ZERO: {}".format(myValues[0]))
