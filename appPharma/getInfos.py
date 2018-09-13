import re

units = re.compile("([\d+,\d+|\d+.\d+|\d+]+\s*[a-zA-Z]+[/[a-zA-Z]+]*)")

test = """
bla 100 mg/mL bla
Bla 0,5 mEq/kg/h bla
bla 25mg/ml bla
bla 0.3 mmol/h/kg bla
bla 48,5 g bla
Bla 0,05 mg/ml bla
bla 51 mg bla    
"""
print(units.findall(test))