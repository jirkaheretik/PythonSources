from pprint import pprint

class Node:
    """
    name
    dir T/F
    size
    content []
    parent
    """
    
    def Node(self, name, size = None, parent = None):
        _name = name
        _parent = parent
        _dir = size == True
        _size = size
        
    def getSize(self):
        pass
# END of class Node

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    
def buildTree(load):

    pass
    
def processValues1(load):
    score = 0
    for i in range(len(load)):
        subs = load[i:i + 4]
        print(f"Substr {subs}")
        pocet = len(set(subs))
        if pocet == 4:
            print("Voila!")
            return i + 4
        
    return score

def processValues2(load):
    score = 0
    for i in range(len(load)):
        subs = load[i:i + 14]
        print(f"Substr {subs}")
        pocet = len(set(subs))
        if pocet == 14:
            print("Voila!")
            return i + 14
    return score

if __name__ == "__main__":
    myValues = readFile("d07.txt")
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("First pkt marker after {} characters".format(result1))
    print("First msg marker after {} characters".format(result2))

