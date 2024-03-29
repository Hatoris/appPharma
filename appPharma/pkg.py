from functools import wraps
from pint.converters import ScaleConverter
from pint.unit import UnitDefinition
import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

ureg.default_format = "P"
#define bmi
ureg.define('bmi = kg/m**2')
#define percent, pct
ureg.define(UnitDefinition('percent', 'pct',  (), ScaleConverter(1 / 100.0)))
#define mEq
ureg.define(UnitDefinition('equivalent', 'Eq',  (), ScaleConverter(1), reference="Quantity"))
#define ounce liquide
ureg.define('ozl = 29.5735293017338 * milliliter = ounce_liquid') 