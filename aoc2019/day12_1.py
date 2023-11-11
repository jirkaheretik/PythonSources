"""
INPUT:
Io, Europa, Ganymede, and Callisto.
17 -9   4
 2  2 -13
-1  5  -1
 4  7  -7
"""

class Moon:
    def __init__(self, name):
        self.name = name
        self.speedX = 0
        self.speedY = 0
        self.speedZ = 0

    def setVelocity(self, x, y, z):
        self.speedX = x
        self.speedY = y
        self.speedZ = z

    def setPos(self, x, y, z):
        self.posX = x
        self.posY = y
        self.posZ = z

    def step(self):
        self.posX += self.speedX
        self.posY += self.speedY
        self.posZ += self.speedZ

    def getEnergy(self):
        return (abs(self.posX) + abs(self.posY) + abs(self.posZ)) * (abs(self.speedX) + abs(self.speedY) + abs(self.speedZ))

    def tisk(self):
        print("{} at [{}, {}, {}] cruising with {}; {}; {} and total energy of {}".format(
            self.name, self.posX, self.posY, self.posZ, self.speedX, self.speedY, self.speedZ, self.getEnergy()))

def compare(m1, m2):
    if m1.posX > m2.posX:
        m1.speedX -= 1
        m2.speedX += 1
    elif m1.posX < m2.posX:
        m1.speedX += 1
        m2.speedX -= 1
    if m1.posY > m2.posY:
        m1.speedY -= 1
        m2.speedY += 1
    elif m1.posY < m2.posY:
        m1.speedY += 1
        m2.speedY -= 1
    if m1.posZ > m2.posZ:
        m1.speedZ -= 1
        m2.speedZ += 1
    elif m1.posZ < m2.posZ:
        m1.speedZ += 1
        m2.speedZ -= 1

def doStep(m1, m2, m3, m4):
    compare(m1, m2)
    compare(m1, m3)
    compare(m1, m4)
    compare(m2, m3)
    compare(m2, m4)
    compare(m3, m4)
    m1.step()
    m2.step()
    m3.step()
    m4.step()

if __name__ == "__main__":
    io = Moon("Io")
    io.setPos(17, -9, 4)
    #io.setPos(-8, -10, 0)
    eu = Moon("Europa")
    eu.setPos(2, 2, -13)
    #eu.setPos(5, 5, 10)
    ga = Moon("Ganymede")
    ga.setPos(-1, 5, -1)
    #ga.setPos(2, -7, 3)
    ca = Moon("Callisto")
    ca.setPos(4, 7, -7)
    #ca.setPos(9, -8, -3)

    for i in range(1000):
        doStep(io, eu, ga, ca)
        if i % 10 == 9:
            print("\nAfter step {}:".format(i + 1))
            io.tisk()
            eu.tisk()
            ga.tisk()
            ca.tisk()
    print("Total energy: {}".format(io.getEnergy() + eu.getEnergy() + ga.getEnergy() + ca.getEnergy()))
