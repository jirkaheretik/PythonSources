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

    def vyloz(self, mnozstvi):
        if mnozstvi <= self._naklad:
            self._naklad -= mnozstvi

    def __str__(self):
        return f"Nákladní auto má naloženo {self._naklad} z možných {self._nosnost} kg."


if __name__ == '__main__':
    tatra = NakladniAuto()
    tatra.naloz(-2000)
    tatra.vyloz(3000)
    print(tatra)
    tatra.naloz(-8000)
    print(tatra)