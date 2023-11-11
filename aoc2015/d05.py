VOWELS = "aeiou"
DISALLOWED = ["ab", "cd", "pq", "xy"]

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    


def processValues1(load):
    """
    Nice strings:
    - no disallowed combinations
    - at least three vowels (aeiou)
    - at least one double letter
    """
    nice = 0
    # cycle all strings
    for string in load:
        # first check forbidden strings, so we do not need to traverse whole string
        hasDis = False
        for item in DISALLOWED:
            if item in string:
                # print(f"{string} contains forbidden value {item}")
                hasDis = True
                break
        if hasDis:
            continue
        vowels = 0
        dblLetter = False
        last = ""
        for c in string:
            if c in VOWELS:
                vowels += 1
            if c == last:
                dblLetter = True
            last = c
        if vowels >= 3 and dblLetter:
            # print(f"Nice: {string}")
            nice += 1
    return nice

def processValues2(load):
    """
    Nice strings:
    - at least one non-overlapping pair of letters appearing twice in the string
    - at least one combination ANA where A is any letter, N a single letter - like xyx, ana, aaa, dod etc.
    """
    print("\n\nProcessing 2:\n\n")
    nice = 0
    # cycle all strings
    for string in load:
        hasANA = False
        hasPair = False
        # process:
        delka = len(string)
        for i in range(delka-2):
            if string[i] == string[i+2]:
                hasANA = True
            dummy = string[i] + string[i+1]
            if dummy in string[i+2:]:
                hasPair = True
        
        if hasANA and hasPair:
            print(f"Nice: {string}")
            nice += 1
        
    return nice


if __name__ == "__main__":
    myValues = readFile("d05.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Nice strings: {}".format(result1))
    print("Nice strings revisited: {}".format(result2))
