from appPharma import pkg
import re
import appPharma.calculPharma

def changeUnits(*units, **kunits):
    """This function @changeUnits('kg', 'umol/l', d = 'unityouwant', z = 'ignore' ) to change unit as wich"""
    def units_decorator(func):
        @pkg.wraps(func)
        def func_wraper(*unit, **kunit):
            values = [] 
            kvalues = {}
            for i in range(len(unit)):
                if units[i] != 'ignore':
                    values.append(formater(unit[i]).to(units[i]))
                else:
                    values.append(formater(unit[i]))
            if kunit is not None:
                for key in kunit:
                    if kunits[key] != 'ignore':
                        kvalues[key] = formater(kunit[key]).to(kunits[key])
                    else:
                        kvalues[key] = formater(kunit[key]) 
            return func(*values, **kvalues)
        return func_wraper
    return units_decorator


def formater(unit):
    """this function match pattern and return pint.quantity"""
    if re.match("\d+[a-zA-Z]+[/|\*]\d+[a-zA-Z]+", unit):
        unit1, unit2 = re.findall("\d+[a-z]*", unit)
        A = pkg.ureg(unit1)
        B = pkg.ureg(unit2)
        if re.search("/", unit):
            return A/B
        elif re.search("\*", unit):
            return A*B
    if re.match("\d+'\d+", unit):
        foot, inch = re.findall("\d+", unit)
        size = pkg.ureg(foot + "foot").to("inch") + pkg.ureg(inch + "inch")
        return size
    return pkg.ureg(unit)