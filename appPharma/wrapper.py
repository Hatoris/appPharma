from appPharma import pkg
import re

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
                        if str(type(kunit[key])) != "<class 'bool'>":
                            kvalues[key] = formater(kunit[key])
                        else:
                            kvalues[key] = kunit[key]
            return func(*values, **kvalues)
        return func_wraper
    return units_decorator


def formater(unit):
    """this function match pattern and return pint.quantity"""
    #unit = unit.replace(",", ".")
    if isinstance(unit, str):
        if re.match(r"((\d+\.\d+|\d+)[a-zA-Z]+[/|\*](\d+\.\d+|\d+)[a-zA-Z]+)", unit):
            unit1, unit2 = map(
                        pkg.ureg, 
                        re.findall(
                         r"(\d+[\.|\,]\d+[a-zA-Z]*|\d+[a-zA-Z]*)", 
                         unit))                   
            if re.search(r"/", unit):
                return unit1/unit2
            elif re.search ("\*", unit):
                return unit1*unit2
        if re.match("\d+'\d+", unit):
            foot, inch = map(pkg.ureg, [a+b for a, b in zip(re.findall("\d+", unit), ["foot", "inch"])]) 
            size = foot.to("inch") + inch
            return size
        if pkg.ureg(unit).units == "percent":
            con = pkg.ureg(unit).magnitude / 100
            return pkg.ureg(str(con) + "g/ml")
        return pkg.ureg(unit)

