#wrraper function
from appPharma import pkg


def changeUnit(*units):
    "use it above function @changeUnit(u1, ux) to change unit as wich" 
    def units_decorator(func):
        def func_wraper(*unit):
            values = []
            for i in range(len(unit)):
                if units[i] != 'ignore':
                    values.append(Q_(unit[i]).to(units[i]))
                else:
                    values.append(unit[i])
            return func(*values)        
        return func_wraper
    return units_decorator

def sameUnits():
    def units_decorator(func):
        def func_wraper(*unit):
            values = []
            for i in range(len(unit)):
                values.append(Q_(unit[i]).to(units[i]))
            return func(*values)        
        return func_wraper
    return units_decorator

def changeUnits(*units, **kunits):
    """use it above function @changeUnits('kg', 'umol/l', d = 'unityouwant', z = 'ignore' ) to change unit as wich"""
    def units_decorator(func):
        @pkg.wraps(func)
        def func_wraper(*unit, **kunit):
            values = [] 
            kvalues = {}
            #k = list(kunit.keys())
            #k.sort() 
            for i in range(len(unit)):
                if units[i] != 'ignore':
                    values.append(pkg.Q_(unit[i]).to(units[i]))
                else:
                    values.append(unit[i])
            if kunit is not None:
                for key in kunit:
                    if kunits[key] != 'ignore':
                        kvalues[key] = pkg.Q_(kunit[key]).to(kunits[key])
                    else:
                        kvalues[key] = kunit[key]
            return func(*values, **kvalues)
        return func_wraper
    return units_decorator