class Pes:
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek

    def zestarni(self):
        self._vek += 1

    def __str__(self):
        return f"{self._jmeno} ({self._vek})"


class Osoba:
    def __init__(self, jmeno):
        self._jmeno = jmeno
        self.pes = None

# MAIN:
azor = Pes("Azor", 3)
pepik = Osoba("Pepik")
pepik.pes = azor
marketka = Osoba("Markéta")
marketka.pes = azor
print(azor)
print(marketka.pes)
marketka.pes.zestarni()
pepik.pes.zestarni()
print(marketka.pes)
