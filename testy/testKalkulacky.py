import unittest
from Kalkulacka import Kalkulacka


class MyTestCase(unittest.TestCase):
    def xtest_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_scitani(self):
        k = Kalkulacka()
        self.assertEqual(42, k.secti(11, 31))
        self.assertEqual(42, k.secti(-9, 51))
        self.assertEqual(42, k.secti(333, -291))

    def test_nasobeni(self):
        k = Kalkulacka()
        self.assertEqual(42, k.vynasob(42, 1))
        self.assertEqual(42, k.vynasob(-6, -7))
        self.assertEqual(42, k.vynasob(21, 2))


    def test_deleni(self):
        k = Kalkulacka()
        self.assertEqual(42, k.vydel(42, 1))
        self.assertEqual(42, k.vydel(-420, -10))
        self.assertEqual(42, k.vydel(21, 0.5))


if __name__ == '__main__':
    unittest.main()
