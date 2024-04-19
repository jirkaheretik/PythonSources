class Clovek:
    _pocet_lidi = 0
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        Clovek._pridej_cloveka()

    def __str__(self):
        return f"Jsem {self.jmeno} a je mi {self.vek} let"

    @staticmethod
    def get_pocet_lidi():
        return Clovek._pocet_lidi

    @staticmethod
    def _pridej_cloveka():
        Clovek._pocet_lidi += 1


def vyberKarla(x):
    return x.jmeno == "Karel"

def vyberPetipismenne(y):
    return len(y.jmeno) == 5

def vyberDlouhaJmena(z):
    return len(z.jmeno) > 5

lide = []
lide.append(Clovek("Karel", 42))
lide.append(Clovek("Josef", 39))
lide.append(Clovek("Filip", 22))
lide.append(Clovek("Markéta", 24))
lide.append(Clovek("Bolehlavoslava", 51))
lide.append(Clovek("Karel", 42))
lide.append(Clovek("Karel", 42))
lide.append(Clovek("Karel", 42))
lide.append(Clovek("Karel", 42))

for c in lide:
    print(c)
print()

#vystup = list(filter(vyberPetipismenne, lide))
#vystup = list(filter(vyberKarla, lide))
#vystup = list(filter(vyberDlouhaJmena, lide))
vystup = list(filter(lambda x: "a" in x.jmeno, lide))
for c in vystup:
    print(c)
