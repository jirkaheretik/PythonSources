# jen komentář

class Zvire:
    def __init__(self, popis, vaha):
        self._popis = popis
        self._vaha = vaha

    @property
    def leta(self):
        return self._vaha < 9

    def nakrm(self, jidlo):
        if jidlo > 0:
            self._vaha += jidlo
    def vypis(self):
        print(self)

    def mluv(self):
        return ""

    def __str__(self):
        return f"Jsem {self._popis}, vážím {self._vaha} kg a " + ("létám" if self.leta else "nelétám")

class Pes(Zvire):
    def __init__(self, popis, vaha, obojek):
        super().__init__(popis, vaha)
        self._obojek = obojek

    def mluv(self):
        return "Haf haf!"

class Kocka(Zvire):
    def __init__(self, popis, vaha, zivoty):
        super().__init__(popis, vaha)
        self._zivoty = zivoty

    def mluv(self):
        return "Mňaauu :-P"

class Krava(Zvire):
    def __init__(self, popis, vaha, dojivost):
        super().__init__(popis, vaha)
        self._litry = dojivost

    def mluv(self):
        return "Bůůůůů"



if __name__ == '__main__':
    vrana = Zvire("vrana", 7)
    vrana.vypis()
    vrana.nakrm(3)
    vrana.vypis()
    zoo = [Pes("Alik", 11, True), Kocka("Micka", 6, 7), Krava("Stračena", 222, 11), vrana, Pes("Fousek", 20, False)]

    for zvire in zoo:
        print(zvire)
        print(zvire.mluv())

