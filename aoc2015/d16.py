"""
Right aunt Sue:
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues

def processValues1(load):
    score = 0
    return score

def processValues2(load):
    score = 0
    return score

if __name__ == "__main__":
    myValues = readFile("d16.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Sue: {}".format(result1))
    print("Sue: {}".format(result2))

