def passes(val):
    adjacentOk = False
    strVal = str(val)
    maxLen = len(strVal)
    for i in range(0, maxLen - 1):
        if strVal[i+1] < strVal[i]:
            return False
        if not adjacentOk and strVal[i] == strVal[i+1]:
            adjacentOk = True
    return adjacentOk


if __name__ == "__main__":
    MIN = 271973
    MAX = 785961
    #MIN = 123
    #MAX = 435

    count = 0
    for i in range(MIN, MAX + 1):
        if passes(i):
            print("Found {}".format(i))
            count += 1
    print("\nTotal number of OK values: {}".format(count))
