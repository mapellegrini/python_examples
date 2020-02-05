#!/usr/bin/python

from re import split as regexsplit
import math 
from inspect import getmembers, isbuiltin 

operators = r"><+()*/^".split()
delims = r'(>+|<+|\++|[A-Z, a-z]*\(+|\)+|/+|\*+|\^+|)'

def mtok(equation_str):
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
    finally:
        return True 

def gettoktype(token):
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

    
eqstr="5*cos(4+4)/arctan(4*5)^(2+2)"
funcname2func_dict=get_funcname2func_dict()
tokens =mtok(eqstr)
stack = []
branch = [] 

for tok in tokens:
    toktype=gettoktype(tok)
    if (toktype==

