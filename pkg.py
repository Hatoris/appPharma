import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

#define bmi
ureg.define('bmi = kg/m**2')
ureg.define('percent = pct = %')

from functools import wraps