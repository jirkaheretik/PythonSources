from copy import copy
from copy import deepcopy
SMERY = {"N": "sever", "S": "jih", "W": "západ", "E": "východ"}
INDEXY = ["N", "S", "W", "E"]

def findSmer(smer):
    for sm, desc in SMERY.items():
        if desc == smer:
            return sm
    return None

class Lokace:
    def __init__(self, nazev, popis):
        self._nazev = nazev
        self._popis = popis
        self.okoli = {"N": None, "S": None, "W": None, "E": None}

    def __str__(self):
        result = f"{self._nazev}\n{self._popis}\n\nMůžeš jít na "
        for smer, lokace in self.okoli.items():
            if lokace is not None:
                result += f"{SMERY[smer]} "
        return result

class Hra:
    def __init__(self):
        # hrad:
        self.hrad = Lokace("Hrad", "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti.\nKlíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
        # les
        self.les = Lokace("Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
        self.rybnik = Lokace("Rybník", "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
        self.rozcesti = Lokace("Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
        self.dum = Lokace("Dům", "Stojíš před svým rodným domem, cítíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dveří.")

        self._pocatek = deepcopy(self.dum)
        self._aktualni = self._pocatek
        hrad = deepcopy(self.hrad)
        les = deepcopy(self.les)
        les2 = deepcopy(self.les)
        les3 = deepcopy(self.les)
        rybnik = deepcopy(self.rybnik)
        les.okoli["W"] = hrad
        hrad.okoli["E"] = les
        rozcesti = deepcopy(self.rozcesti)
        les.okoli["E"] = rozcesti
        rozcesti.okoli["W"] = les
        rozcesti.okoli["E"] = les2
        rozcesti.okoli["S"] = les3
        les2.okoli["W"] = rozcesti
        les2.okoli["E"] = rybnik
        rybnik.okoli["W"] = les2
        les3.okoli["N"] = rozcesti
        les3.okoli["E"] = self._pocatek
        self._pocatek.okoli["W"] = les3

    def posun(self, cmd):
        if cmd in INDEXY:
            self._aktualni = self._aktualni.okoli[cmd]
        return self._aktualni

    def pocatek(self):
        return self._pocatek

#MAIN:
hra = Hra()
pozice = hra.pocatek()
while (True):
    print(pozice)
    cmd = input("\nZadej příkaz: ").lower()
    if cmd == "konec":
        break
    if cmd.startswith("jdi na "):
        smer = cmd[7:].strip()
        dir = findSmer(smer)
        if dir is None:
            print(f"Neznámý směr {smer}")
        elif pozice.okoli[dir] is None:
            print(f"Tímto směrem nelze jít.")
        else:
            pozice = hra.posun(dir)
    else:
        print("Můj vstupní slovník neobsahuje tento příkaz.")
