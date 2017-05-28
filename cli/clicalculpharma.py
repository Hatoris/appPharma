"""cli application to perform calcul

Usage:
    calculPharma bmi (--infos | <weight> <size>)
    calculPharma iw (--infos | <size> [--sex])
    calculPharma bsa (--infos | <weight> <size>)
    calculPharma content (--infos | <mass> <volume>)
    calculPharma aw (--infos | <weight> <idealweightorsize> [--sex])
    calculPharma clairance (--infos | <age> <weight> <creatine> [<size> --sex --min]) 

Options:
    -h --help    choose one Calcul from Calcul pharma to perform
    -i --infos   give information on calcul
    -s --sex     sex of patient by default: F = False
    -m --min    time in second by default or in minute if set to True
    


Informations:
    weight = patient weight in kg, lb, g ...
    size = patient size in m, cm, foot, inch
    sex = by default sexe is man if set to True sex is woman
    mass = mass of compound in lb, g ...
    volume = volume of solution in mL, ozlquide, L ...
    age = patient age
    creatine = dosage of patient's creatine in mol/L

"""

import docopt
import appPharma.calculPharma

if __name__ == "__main__":
    args = docopt.docopt(__doc__, version='0.1')

    if args['bmi']:
        if args["--infos"]:
            help(appPharma.calculPharma.bmi)
        else:
            print(appPharma.calculPharma.bmi(args["<weight>"], args["<size>"]))
    elif args['iw']:
        if args["--infos"]:
            help(appPharma.calculPharma.iw)
        else:
            print(appPharma.calculPharma.iw(args["<size>"], F = args["--sex"]))
    elif args['bsa']:
        if args["--infos"]:
            help(appPharma.calculPharma.bsa)
        else:
            print(appPharma.calculPharma.bsa(args["<weight>"], args["<size>"]))
    elif args['content']:
        if args["--infos"]:
            help(appPharma.calculPharma.content)
        else:
            print(appPharma.calculPharma.content(args["<mass>"], args["<volume>"]))
    elif args['aw']:
        if args["--infos"]:
            help(appPharma.calculPharma.aw)
        else:
            print(appPharma.calculPharma.aw(args["<weight>"], args["<idealweightorsize>"], F = args["--sex"]))
    elif args['clairance']:
        if args["--infos"]:
            help(appPharma.calculPharma.clairanceC)
        else:
            if args["<size>"]:
                print(appPharma.calculPharma.clairanceC(int(args["<age>"]), args["<weight>"], args["<creatine>"], F=args["--sex"],min=args["--min"], size=args["<size>"]))
            else:
                print(appPharma.calculPharma.clairanceC(int(args["<age>"]), args["<weight>"], args["<creatine>"], F=args["--sex"], min=args["--min"]))

