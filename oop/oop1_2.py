class Kalkulacka:
    a = None
    b = None
    # Zde dokonči úlohu svým kódem...
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def secti(self):
        return self.a + self.b

    def odecti(self):
        return self.a - self.b

    def vynasob(self):
        return self.a * self.b

    def vydel(self):
        return self.a / self.b

    def __str__(self):
        return f"Součet: {self.secti()}\nRozdíl: {self.odecti()}\nSoučin: {self.vynasob()}\nPodíl: {self.vydel()}"

def kalkulacka_main():
    x = float(input("Zadej 1. číslo:\n"))
    y = float(input("Zadej 2. číslo:\n"))
    k = Kalkulacka(x, y)
    print(k)


class NakladniAuto:

    def __init__(self, nosnost = 3000):
        """
        Vytvoří novou instanci nákladního auta
        :param nosnost: Maximální nosnost daného auta, defaultní hodnota 12 t
        """
        self._nosnost = nosnost
        self._naklad = 0

    def naloz(self, mnozstvi):
        if self._naklad + mnozstvi <= self._nosnost:
            self._naklad += mnozstvi

    def vyloz(self, mnozstvi):
        if mnozstvi <= self._naklad:
            self._naklad -= mnozstvi

    def getNaklad(self):
        return self._naklad

    def __str__(self):
        return f"V nákladním autě je naloženo {self._naklad} kg"

    def vypis(self):
        print(self)

def nakladak_main():
    tatra = NakladniAuto()
    tatra.naloz(10000)
    tatra.naloz(500)
    tatra.vyloz(300)
    tatra.vyloz(1000)
    print(tatra)

class Kamarad:
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek
        self._kamarad = None

    def skamarad_se(self, clovek):
        self._kamarad = clovek

    def __str__(self):
        return (f"Ahoj, já jsem {self._jmeno}, je mi {self._vek} let" +
        (f" a můj kamarád je {self._kamarad._jmeno}" if self._kamarad is not None else ""))

def kamaradi_main():
    karel = Kamarad("Karel Novák", 33)
    cyril = Kamarad("Cyril Nový", 27)
    print(karel)
    print(cyril)
    karel.skamarad_se(cyril)
    cyril.skamarad_se(karel)
    print(karel)
    print(cyril)


if __name__ == '__main__':
    # kalkulacka_main()
    # nakladak_main()
    kamaradi_main()
    pass