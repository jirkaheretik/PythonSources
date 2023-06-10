import unittest

from Kalkulacka import Kalkulacka
class MyTestCase(unittest.TestCase):
    def nontest_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_scitani(self):
        k = Kalkulacka()
        self.assertEqual(42, k.secti(11, 31))
        self.assertEqual(42, k.secti(-9, 51))
        self.assertEqual(42, k.secti(333, -291))


if __name__ == '__main__':
    unittest.main()
