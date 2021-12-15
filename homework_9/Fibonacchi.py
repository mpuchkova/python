def Fibonacchi_number(x):
    """"return Fibonachi numbers by number"""
    x=int(x)
    if x in (1, 2):
        return 1
    else:
        return Fibonacchi_number(x - 1) + Fibonacchi_number(x - 2)