import unittest

from NakladniAuto import NakladniAuto, NakladException


class NakladakTestCase(unittest.TestCase):
    def test_prazdne_na_zacatku(self):
        instance = NakladniAuto()
        self.assertEqual(0, instance.getNaklad())

    def test_vylozeni(self):
        instance = NakladniAuto()
        instance.naloz(5000)
        instance.vyloz(3000)
        self.assertEqual(2000, instance.getNaklad())

    def test_vylozeni_pod_nulu(self):
        instance = NakladniAuto()
        instance.naloz(5000)
        self.assertRaises(NakladException, instance.vyloz, 8000)

    def test_nosnost_default(self):
        instance = NakladniAuto()
        instance.naloz(10000)
        #instance.naloz(5000)
        #self.assertEqual(10000, instance.getNaklad())
        #self.assertRaises(NakladException, instance.naloz, 5000)

    def xtest_nosnost_default_zaklad(self):
        instance = NakladniAuto()
        instance.naloz(15000)
        self.assertEqual(0, instance.getNaklad())

    def xtest_nosnost_vlastni(self):
        instance = NakladniAuto(5000)
        instance.naloz(4000)
        instance.naloz(4000)
        self.assertEqual(4000, instance.getNaklad())


if __name__ == '__main__':
    unittest.main()
