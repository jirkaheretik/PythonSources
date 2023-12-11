# Part 1 - Easy (Clovek, Clovek, jejich Pes, zestarnout, vypsat)
class Osoba:
    def __init__(self, name):
        self._name = name
        self._pes = None

    def pridej(self, pes):
        self._pes = pes

    def getPes(self):
        return self._pes

class Pes:
    def __init__(self, name):
        self._name = name
        self._vek = 1

    def __str__(self):
        return f"{self._name} ({self._vek})"

    def zestarni(self):
        self._vek += 1

def easy():
    karel = Osoba("Karel Novák")
    lenka = Osoba("Lenka Nováková")
    azor = Pes("Azor")
    print(azor)
    karel.pridej(azor)
    lenka.pridej(azor)
    karel.getPes().zestarni()
    lenka.getPes().zestarni()
    print(azor)


# Part 2 - Hra (Lokace, Hra, Prochazeni)

def mid():
    pass

if __name__ == '__main__':
    easy()