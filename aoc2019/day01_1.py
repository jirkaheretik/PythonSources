def getFuel(mass):
    result = mass // 3
    return max(result - 2, 0)

def sumUp(values):
    sum = 0
    for item in values:
        sum += getFuel(item)
    return sum

def readFile(filename):
    inputValues = list()
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.readlines()
        for x in contents:
            print("Adding {} from input.".format(x))
            inputValues.append(int(x))
    return inputValues


if __name__ == "__main__":
    print("Sum of fuel requirements: {}".format(sumUp(readFile("d01input.txt"))))
