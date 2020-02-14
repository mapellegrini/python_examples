#!/usr/bin/python -B

from re import split as regexsplit
from math import * 
from inspect import getmembers, isbuiltin 
import operator
import sys


def mtok(equation_str):
    delims =r'(>+|<+|\++|[A-Z, a-z]*\(|\)|/+|\*|\^+|-|)'
    equation_str = equation_str.replace(" ", "")
    tokens=regexsplit(delims, equation_str)
    tokens = [x for x in tokens if x not in ""]
    return tokens

def get_funcname2func_dict():
    funcname2func={}
    for functionname in [item[0] for item in getmembers(math, isbuiltin)]:
        funcname2func[functionname]=getattr(math, functionname)
    return funcname2func

def isnum(val):
    try:
        float(val)
    except ValueError:
        return False
    return True 

def gettoktype(tok):
    operators = list("><+-()*/^")
    if (isnum(tok)):
        return "num"
    elif (tok in operators):
        return "operator"
    elif(tok == "("):
        return "oparen"
    elif(tok.endswith("(")):
        return "func"
    elif(tok == ")"):
        return "cparen" 
    else: #unknown variable 
        return "var" 

def getvars(eq):
    tokens = mtok(eq)
    variables = [] 
    for tok in tokens:
        toktype = gettoktype(tok)
        #print tok, toktype
        if (gettoktype(tok) == "var") and (variables.count(tok) == 0):
            variables.append(tok)
    #print "found variables:", variables
    return variables


def eqstr2func(eq, forceparam=False):
    params = getvars(eq)
    if (forceparam and not params):
        params = ["x"]
    defstr = "def newfunc(" + ",".join(params) + "):\n\treturn " + eq
    exec(defstr)
    return locals()["newfunc"]


if __name__ == "__main__":
    eq1 = "cos(2+3*4^(5+6*x))"
    eq2 = "1+2+3+4"
    eq3 = "sqrt(x+y)"
    eq4 = "abs(x)"

    func1=eqstr2func(eq1)
    func2=eqstr2func(eq2)
    func3=eqstr2func(eq3)
    func4=eqstr2func(eq4)

    print func1(0)
    print func2()
    print func3(2,7)
    print func4(-4)
