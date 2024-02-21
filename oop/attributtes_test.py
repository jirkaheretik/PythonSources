class Clovek:
    jmeno = "Noname"
    vek = None
    unava = 10

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def spi(self, doba):
        self.unava -= doba * 10
        if self.unava < 0:
            self.unava = 0

    def behej(self, vzdalenost):
        if self.unava + vzdalenost <= 20:
            self.unava += vzdalenost
        else:
            print("Jsem příliš unavený")

    def __str__(self):
        return f"{self.jmeno} {self.vek} s únavou {self.unava}"

if __name__ == '__main__':
    karel = Clovek("Karel", 42)
    print(karel)
    karel.behej(15)
    karel.spi(5)
    print(karel)
    pepik = Clovek("Josef", 23)
    print(pepik)
    print(karel)
    karel.behej(20)
    print(pepik)
    print(karel)
    print(Clovek.unava)
    print(Clovek.jmeno)
