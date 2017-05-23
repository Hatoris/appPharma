import appPharma.calculPharma
import appPharma.pkg
import unittest

"""
    M = man : F = False
    F = woman : F = True
    Out = ignore kwargs
"""

class CalculPharmaTest(unittest.TestCase):

    def setUp(self):
        #Body Mass Index
        self.bmi = appPharma.calculPharma.bmi('80kg', '180cm')
        #Body Surface Area
        self.bsa = appPharma.calculPharma.bsa('200lb', '66inch')
        #content
        self.content = appPharma.calculPharma.content('10oz', '1l')
        #Ideal weight
        self.iwM = appPharma.calculPharma.iw('180cm')
        self.iwF = appPharma.calculPharma.iw('66inch', F = True)
        self.iwMM = appPharma.calculPharma.iw('5.7foot', F = False)
        #Adjusted weight
        self.awSizeOutM = appPharma.calculPharma.aw('180lb', '66inch')
        self.awSizeM = appPharma.calculPharma.aw('90kg', '180cm', F = False)
        self.awSizeF = appPharma.calculPharma.aw('90000g', '1.80m', F = True)

    
    def test_bmi(self):
        self.assertEqual(self.bmi, appPharma.pkg.ureg('24.691358024691358 kilogram / meter ** 2'))

    def test_bsa(self):
        self.assertEqual(self.bsa, appPharma.pkg.ureg('2.0553483741854244 meter ** 2'))

    def test_content(self):
        self.assertEqual(self.content, appPharma.pkg.ureg('28.349523125000005 percent'))

    def test_iw(self):
        self.assertEqual(self.iwM, appPharma.pkg.ureg('74.99212598425197 kilogram'))
        self.assertEqual(self.iwF, appPharma.pkg.ureg('59.3 kilogram'))
        self.assertEqual(self.iwMM, appPharma.pkg.ureg('69.32000000000001 kilogram'))

    def test_aw(self):
        self.assertEqual(self.awSizeOutM, appPharma.pkg.ureg('70.93865064 kilogram'))
        self.assertEqual(self.awSizeM, appPharma.pkg.ureg('80.99527559055119 kilogram'))
        self.assertEqual(self.awSizeF, appPharma.pkg.ureg('78.29527559055119 kilogram'))

if __name__ == '__main__':
    unittest.main()

