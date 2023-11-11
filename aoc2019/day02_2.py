from random import randint
import copy
import sys

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
            else:
                print("Unknown instruction {}, exitting.".format(instruction))
                return
        except KeyError:
            print("Attempt to read unknow address {}, exitting.".format(start))
            return

def initialization(values, noun, verb):
    values[1] = noun
    values[2] = verb

if __name__ == "__main__":
    EXPECTED = 19690720
    MAX = 99
    initValues = readFile("d02input.txt")
#    while True:
    for noun in range(MAX):
        for verb in range(MAX):
#        noun = randint(0, MAX)
#        verb = randint(0, MAX)
            myValues = copy.copy(initValues)
            initialization(myValues, noun, verb)
            processValues(myValues, 0)
            if myValues[0] == EXPECTED:
                print("Voila!!! We are looking for {}".format(noun * 100 + verb))
                sys.exit()
            print("NO: {}-{}.".format(noun, verb))
