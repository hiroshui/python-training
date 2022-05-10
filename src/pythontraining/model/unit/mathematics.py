# mathematics.py
import math


def multiply(x, y):
    return x * y

#def divide(x, y):
#    return x / y

def round_up(x):
    rounded = math.ceil(x) #int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded

def divide(x, y):
    erg = x / y
    return round(erg, 1)

def hypotenuse(a, b):
    a_sqrd = int(a) * int(a)
    b_sqrd = int(b) * int(b)
    print(f"a² = {a_sqrd}, b² = {b_sqrd}")
    c_srqd = int(a_sqrd + b_sqrd)
    c = math.sqrt(c_srqd)
    return round(c,2)