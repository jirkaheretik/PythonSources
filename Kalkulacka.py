class Kalkulacka:
    def secti(self, a, b):
        return a + b

    def odecti(self, a, b):
        return a - b

    def vynasob(self, a, b):
        return a * b

    def vydel(self, a, b):
        return a / b


if __name__ == '__main__':
    k = Kalkulacka()
    print(k.secti(5, 10))
    print(k.odecti(20, -10))