from pprint import pprint
# from numpy import sign
import math


def sg(x):
    return (x > 0) - (x < 0)

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    

def processValues1(load):
    score = 0
    cycle = 0
    register = 1
    nextStop = 20
    for instruction in load:
        toAdd = 0
        if instruction == "noop":
            cycle += 1
        elif instruction[:4] == "addx":
            toAdd = int(instruction[5:])
            cycle += 2
        else:
            print(f"Unknown instruction {instruction}")
        if cycle >= nextStop:
            score += register * nextStop
            nextStop += 40
            if nextStop > 250:
                break 
        register += toAdd 

    return score
    
def processValues2(load):
    score = 0
    cycle = 0
    register = 1
    output = ""
    for instruction in load:
        toAdd = 0
        if instruction == "noop":
            output += "#" if abs(register - (cycle % 40)) <= 1  else "." 
            cycle += 1
        elif instruction[:4] == "addx":
            toAdd = int(instruction[5:])
            for i in range(2):
                output += "#" if abs(register - (cycle % 40)) <= 1  else "." 
                cycle += 1

        else:
            print(f"Unknown instruction {instruction}")
        register += toAdd 
    for i in range(6):
        print(output[40*i:40*i+40])    
    return score

if __name__ == "__main__":
    myValues = readFile("d10.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Sum of signal strengths: {}".format(result1))
    #print("Long tail positions {}".format(result2))

