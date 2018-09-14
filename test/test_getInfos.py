from appPharma import getInfos as gi
from appPharma.pkg import ureg
import unittest
import re

class TestGetInfos(unittest.TestCase):

    def setUp(self):
        self.test = """
            bla 100 mg/mL bla
            Bla 0,5 mEq/kg/h bla
            bla 25mg/ml bla
            bla 0.3 mmol/h/kg bla
            bla 48,5 g bla
            Bla 0,05 mg/ml bla
            bla 51 mg bla
            bla 0.5 g bla
            bla 123 mg/12mL bla
            bla 0,5mg/0,2mg bla
            bla 12mmol/34g/0.2mg bla
            bla 12 % bla
            bla 0,5 % bla
            bla 12,5 mg/34% bla
        """

    def test_units(self):
        self.assertEqual(
            gi.extract_infos(self.test), [
                '100 mg/mL', 
                '0,5 mEq/kg/h', 
                '25mg/ml', 
                '0.3 mmol/h/kg', 
                '48,5 g', 
                '0,05 mg/ml',
                 '51 mg', 
                 '0.5 g', 
                 '123 mg/12mL', 
                 '0,5mg/0,2mg', 
                 '12mmol/34g/0.2mg',
                 '12 %',
                 '0,5 %',
                 '12,5 mg/34%'
            ])


if __name__ == "__main__":
    unittest.main()
