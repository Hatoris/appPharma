"""cli application to perform calcul

Usage:
    calculPharma bmi <weight> <size>
    calculPharma iw <size> [--sex <sex>]
    calculPharma bsa <weight> <size>
    calculPharma content <mass> <volume>
    calculPharma aw <weight> (<idealweight> | <size> [--sex <sex>])

Options:
    -h --help    choose one Calcul from Calcul pharma to perform
    -sx --sex     sex of patient by default: F = False


Informations:
    weight = patient weight in kg, lb, g ...
    size = patient size in m, cm, foot, inch
    sex = by default sexe is man if set to True sex is woman
    mass = mass of compound in lb, g ...
    volume = volume of solution in mL, ozlquide, L ...

"""

import docopt
import appPharma.calculPharma

if __name__ == "__main__":
    args = docopt.docopt(__doc__, version='0.1')

    if args['bmi']:
        print(appPharma.calculPharma.bmi(args["<weight>"], args["<size>"]))
    elif args['iw']:
        print(appPharma.calculPharma.iw(args["<size>"], F = args["<sex>"]))
    elif args['bsa']:
        print(appPharma.calculPharma.bsa(args["<weight>"], args["<size>"]))
    elif args['content']:
        print(appPharma.calculPharma.content(args["<mass>"], args["<volume>"]))
    elif args['aw']:
        if args['<idealweight>']:
            print(appPharma.calculPharma.aw(args["<weight>"], args["<idealweight>"]))
        elif args['<size>']:
            print(appPharma.calculPharma.aw(args["<weight>"], args["<size>"], F = args["<sex>"]))


