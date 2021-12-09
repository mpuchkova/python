def Fibonachi_7(x):
    """"return Fibonachi numbers by number"""
    x=int(x)
    if x in (1, 2):
        return 1
    else:
        return Fibonachi_7(x - 1) + Fibonachi_7(x - 2)


def sum_7(*args):
    """return sum of all arguments"""
    rez=0
    for i in args:
        rez+=i
    return(rez)