from functools import wraps
from pint.converters import ScaleConverter
from pint.unit import UnitDefinition
import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

#define bmi
ureg.define('bmi = kg/m**2')
#define percent, pct
ureg.define(UnitDefinition('percent', 'pct', (), ScaleConverter(1 / 100.0)))
