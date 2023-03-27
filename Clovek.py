class Clovek:
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek

    def pozdrav(self, pozdrav = "Ahoj"):
        print(f"{pozdrav}, já jsem {self._jmeno} a je mi {self._vek} let.")

    def __str__(self):
        return f"{self._jmeno}, {self._vek}"


class Programator(Clovek):
    def __init__(self, jmeno, vek, jazyk):
        super().__init__(jmeno, vek)
        self._jazyk = jazyk
    def pozdrav(self, pozdrav = None):
        if pozdrav is None:
            print("Hello world!")
        else:
            super(Programator, self).pozdrav(pozdrav)

karel = Programator("Karel", 42, "Python")
karel.pozdrav()
karel.pozdrav("Čau")
print(karel)