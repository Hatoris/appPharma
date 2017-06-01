from appPharma import pkg
import appPharma.calculPharma

def changeUnits(*units, **kunits):
    """use it above function @changeUnits('kg', 'umol/l', d = 'unityouwant', z = 'ignore' ) to change unit as wich"""
    def units_decorator(func):
        @pkg.wraps(func)
        def func_wraper(*unit, **kunit):
            values = [] 
            kvalues = {}
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

def convertImperialSize(func):
    def func_wraper(*unit, **kunit):
        values = []
        kvalues = {}
        for i in range(len(unit)):
            try:
                foot, inch = unit[i].split("'")
                values.append(str(appPharma.calculPharma.imperialSize(unit[i], "cm").magnitude) + "cm")
            except: 
                values.append(unit[i])
        if kunit is not None:
            for key in kunit:
                try:
                    foot, inch = kunit[key].split("'")
                    kvalues[key] = str(calculPharma.imperialSize(kunit[key], "cm").magnitude) + "cm" 
                except:
                    kvalues[key] = kunit[key]
        return func(*values, **kvalues)
    return func_wraper

