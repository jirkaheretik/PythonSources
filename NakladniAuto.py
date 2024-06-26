class NakladException(Exception):

    def __init__(self, *args):
        super().__init__(*args)


class NakladniAuto:

    def __init__(self, nosnost = 12000):
        """
        Vytvoří novou instanci nákladního auta
        :param nosnost: Maximální nosnost daného auta, defaultní hodnota 12 t
        """
        self._nosnost = nosnost
        self._naklad = 0

    def naloz(self, mnozstvi):
        if self._naklad + mnozstvi <= self._nosnost:
            self._naklad += mnozstvi
        else:
            raise NakladException("Nevejde se")

    def vyloz(self, mnozstvi = -42):
        if mnozstvi == -42:
            mnozstvi = self._naklad
        if mnozstvi <= self._naklad:
            self._naklad -= mnozstvi
        else:
            raise NakladException("Tolik nevezu")

    def getNaklad(self):
        return self._naklad

    def __str__(self):
        return f"Nákladní auto má naloženo {self._naklad} z možných {self._nosnost} kg."

    def vypis(self):
        print(self)


if __name__ == '__main__':
    tatra = NakladniAuto()
    tatra.naloz(-2000)
    tatra.vypis()
    tatra.vyloz(-300000)
    print(tatra)
    tatra.naloz(8000)
    tatra.naloz(8000)
    tatra.naloz(8000)
    print(tatra)