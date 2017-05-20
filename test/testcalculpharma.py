import appPharma.calculPharma
import appPharma.pkg
import unittest

class CalculPharmaTest(unittest.TestCase):

    def setUp(self):
        self.bmi = appPharma.calculPharma.bmi('80kg', '180cm')
    
    def test_bmi(self):
        self.assertEqual(self.bmi, appPharma.pkg.ureg('24.691358024691358 kilogram / meter ** 2'))

    x

if __name__ == '__main__':
    unittest.main()

