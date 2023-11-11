class Planet:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = list()

    def isRoot(self):
        return self.parent == None

    def getChildren(self):
        return self.children

    def countDirectOrbits(self):
        count = 0
        for obj in self.children:
            count += 1 + obj.countOrbits()
        return count

    def countAllOrbits(self):
        count = 0
        for obj in self.children:
            count += obj.countAllOrbitsWithDepth(1)
        return count

    def countAllOrbitsWithDepth(self, myDepth):
        count = myDepth
        for obj in self.children:
            count += obj.countAllOrbitsWithDepth(myDepth + 1)
        return count

    def showMyLine(self):
        if self.parent == None:
            return self.name + "-"
        else:
            return self.parent.showMyLine() + self.name + "-"

def getPlanet(name):
    if name in Planets:
        print("Found a planet objects {}, obj: {}".format(name, Planets[name]))
        return Planets[name]
    else:
        obj = Planet(name)
        Planets[name] = obj
        print("Creating new planet {}, obj: {}, planet name: {}".format(name, obj, obj.name))
        return obj


def readFile(filename):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.readlines()
        for line in contents:
            #print("Adding {} from input.".format(line))
            (parent, child) = line.split(')')
            pObj = getPlanet(parent.strip())
            chObj = getPlanet(child.strip())
            pObj.children.append(chObj)
            chObj.parent = pObj
    return len(contents)

if __name__ == "__main__":
    Planets = dict()
    lines = readFile("d06input.txt")
    print("Finished the input of {} lines. Found {} planets.".format(lines, len(Planets)))

    #sanity check:
    for planet in Planets:
        if Planets[planet].parent == None:
            print("Planet without parent: {}".format(Planets[planet].name))

    print("Number of all orbits: {}".format(Planets["COM"].countAllOrbits()))

    print(Planets["YOU"].showMyLine())
    print(Planets["SAN"].showMyLine())