class Kouzlo:
    def __init__(self, nazev, typ):
        self._nazev = nazev
        self._typ = typ

    def getNazev(self):
        return self._nazev

    def getTyp(self):
        return self._typ

class Mag:
    def __init__(self, jmeno):
        self._jmeno = jmeno
        self._specailizace = None
        self._typy_kouzel = []

    def setSpecializace(self, specializace):
        self._specailizace = specializace;
        if (specializace == "voda"):
            self._typy_kouzel = ["vodni", "ohnive"]
        elif (specializace == "ohen"):
            self._typy_kouzel = ["temne", "ohnive"]
        elif (specializace == "temna"):
            self._typy_kouzel = ["temne"]
        else:
            self._typy_kouzel = ["ciste"]
        print(f"{self._jmeno} se nyní specializuje na {specializace}")

    def pouzijKouzlo(self, kouzlo):
        if kouzlo.getTyp() in self._typy_kouzel:
            print(f"{self._jmeno} použil kouzlo {kouzlo.getNazev()}")
        else:
            print(f"{self._jmeno} nemůže použít {kouzlo.getNazev()} s typem poškození {kouzlo.getTyp()}")

# MAIN:
koule = Kouzlo("Ohnivá koule", "ohnive")
kletba = Kouzlo("Kletba smrti", "temne")
nula = Kouzlo("Absolutní nula", "vodni")
energie = Kouzlo("Manipulace živé energie", "cista")

mag = Mag("Gandalf")
mag.setSpecializace("voda")
mag.pouzijKouzlo(nula)
mag.pouzijKouzlo(kletba)
mag.setSpecializace("temna")
mag.pouzijKouzlo(kletba)
mag.pouzijKouzlo(energie)
mag.setSpecializace("ohen")
mag.pouzijKouzlo(koule)
