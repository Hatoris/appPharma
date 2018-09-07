import appPharma.wrapper as w
from appPharma.pkg import ureg
import unittest

def func(*args, **kwargs):
    return args, kwargs

def wf(*args, **kwargs):
    T = w.changeUnits(*args, **kwargs)
    U = T(func)
    return U
    
class TestWrapper(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_changeUnits(self):
        lol = wf("kg", "m")
        self.assertEqual(lol("1000g", "100cm"), ((ureg("1kg"), ureg("1m")), {}))
       
    def test_changeUnits_ignore(self):
        lol = wf("kg", "ignore")
        self.assertEqual(lol("1000g", "100cm"), ((ureg("1kg"), ureg("100cm")), {}))
        
    def test_changeUnits_all(self):
        lol = wf("L", "ignore", vol="m**3", taille="um", bob="ignore")
        self.assertEqual(
        lol("1000ml", "100cm", vol="1000L", taille="1000nm", bob="1mg"), 
        (
        ((ureg("1L"), ureg("100cm")), 
        {"vol" : ureg("1m**3"), 
        "taille" : ureg("1um"), 
        "bob" : ureg("1mg")})))
             
if __name__ == "__main__":
    unittest.main()