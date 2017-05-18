from .. import calculPharma
import unittest

class CalculPharmaTest(unittest.TestCase):

    def setUp(self):
        self.bmi = calculPharma.bmi('80kg', '180cm')
    
    def test_bmi(self):
        #res = calculPharma.bmi('80kg', '180cm')
        self.assertEqual(self.bmi, "<Quantity(24.691358024691358, 'kilogram / meter ** 2')>")
        
        
unittest.main()

