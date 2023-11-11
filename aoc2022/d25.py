import math 

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
PLACES = [5**i for i in range(22)]
def snafu2dec(vstup):
    number = 0
    reverse = vstup[::-1]
    for i in range(len(reverse)):
        c = reverse[i]
        if c == "-":
            val = -1
        elif c == "=":
            val = -2
        else:
            val = int(c)
        number += PLACES[i] * val
    return number
    
def dec2snafu(vstup):
    result = ""
    overflow = 0
    end = False
    while vstup > 0 or overflow > 0:
        modulo = (vstup + overflow) % 5
        vstup = (vstup + overflow) // 5
        overflow = 0
        if modulo > 2:
            overflow = 1
            if modulo == 3:
                result += "="
            else:
                result += "-"
        else:
            result += str(modulo)
    return result[::-1]
    
def processValues1(vstup):
    score = 0
    for num in vstup:
        score += snafu2dec(num)
    return dec2snafu(score)
    
def processValues2(vstup):
    score = 0
    return score
    
def testProcess():
    snafuVals = ["1=-0-2", "20012", "1=-1="]
    decVals = [3, 8, 12345, 314159265]
    for s in snafuVals:
        dec = snafu2dec(s)
        snafu = dec2snafu(dec)
        print(f"Original: {s}, dec: {dec}, back to snafu: {snafu}")
    for d in decVals:
        snafu = dec2snafu(d)
        dec = snafu2dec(snafu)
        print(f"Original: {d}, snafu: {snafu}, back to dec: {dec}")

if __name__ == "__main__":
    myValues = readFile("d25.txt")
    #testProcess()
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("SNAFU fuel total: {}".format(result1))
    print("NA: {}".format(result2))

# Failed answers P1: 
# 