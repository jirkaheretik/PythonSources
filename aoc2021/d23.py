import math 

def readFile(filename):
    inputValues = dict()
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
   
def processValues1(vstup):
    score = 0
    return score
    
def processValues2(vstup):
    score = 0
    return score

if __name__ == "__main__":
    myValues = readFile("d23.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Square after 10 rounds: {}".format(result1))
    print("NA: {}".format(result2))

# Failed answers P1: 
# 