from appPharma.convertPharma import convertPharma
from appPharma.pkg import ureg
import unittest


class TestConvertPharma(unittest.TestCase):

    def test_convertPharma_general(self):
        result = convertPharma("180cm to inch, foot, m")
        self.assertEqual(result.value, "180cm")
        self.assertEqual(result.unitToConvert, ["inch", "foot", "m"])
        b = ureg("180cm")
        i = b.to("inch")
        f = b.to("foot")
        m = b.to("m")
        v = list(map(str, [i, f, m]))
        self.assertEqual(result.results, {"180cm" : v})
        l = lambda x : f"180cm = {ureg(x):.2f}" 
        vv = list(map(l, v))
        self.assertEqual(list(result.humanRead), vv)

if __name__ == '__main__':
    unittest.main()

