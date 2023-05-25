"""
Test for __eq__(), which, contrary to other languages:
- calls the same function if comparing c1==c2 and c2==c1 if one object
  is a subclass of other object class (and __eq__ is overridden)
- therefore much harder to break __eq__ contract, though there is actually
  none in Python

"""

class Clovek:
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek

    def pozdrav(self, pozdrav = "Ahoj"):
        print(f"{pozdrav}, já jsem {self._jmeno} a je mi {self._vek} let.")

    def __str__(self):
        return f"{self._jmeno}, {self._vek}"

    def __eq__(self, xxxxx):
        print("Clovek.Eq called %r == %r" % (self, xxxxx))
        if not isinstance(xxxxx, Clovek):
            print("Clovek.Eq - the other object is not Clovek")
            return False
        print("Clovek.Eq - comparing values")
        return self._jmeno == xxxxx._jmeno and self._vek == xxxxx._vek


class Programator(Clovek):
    def __init__(self, jmeno, vek, jazyk):
        super().__init__(jmeno, vek)
        self._jazyk = jazyk
    def pozdrav(self, pozdrav = None):
        if pozdrav is None:
            print("Hello world!")
        else:
            super(Programator, self).pozdrav(pozdrav)
    def __eq__(self, other):
        print("Pgmer.Eq called %r == %r" % (self, other))
        if not isinstance(other, Programator):
            print("Pgmer.Eq - the other object is not Pgmer")
            return False
        print("Pgmer.Eq - comparing values")
        return self._jmeno == other._jmeno and self._vek == other._vek and self._jazyk == other._jazyk

c1 = Clovek("Karel", 42)
c2 = Programator("Karel", 42, "Python")
c3 = c1
print("Začátek")
if c2 == c1:
    print("Stejné")
else:
    print("Různé")

if c1 == c2:
    print("Tohle taky stejné")
else:
    print("Tohle taky různé")
print("Konec.")