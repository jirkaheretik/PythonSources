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
        print(f"Jsem {self._popis}, vážím {self._vaha} kg a " + ("létám" if self.leta else "nelétám"))


if __name__ == '__main__':
    vrana = Zvire("vrana", 7)
    vrana.vypis()
    vrana.nakrm(3)
    vrana.vypis()