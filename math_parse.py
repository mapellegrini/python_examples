#!/usr/bin/python

from re import split as regexsplit
import math 
from inspect import getmembers, isbuiltin 
import operator
import sys

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

def str2func(mylst):
    print "processing:", mylst
    hasvar=False
    for tok in mylst:
        if (gettoktype(tok)=="var"):
            hasvar=True
            break
    if (hasvar):
       print mylst        
    else:
        eqstr="".join(mylst)
        result=eval(eqstr)
        print "Returning", result
        return str(result)


from math import cos

def defstr2func(fnamestr, defstr):
    exec(defstr)
    return

def getvars(eq):
    return "x"	

def eqstr2func(eq):
    defstr = "def newfunc(" + ",".join(getvars(eq)) + "):\n\treturn " + eq
    exec(defstr)
    return locals()["newfunc"]


teq = "cos(2+3*4^(5+6*x))"
fptr = eqstr2func(teq)
print (fptr)
print (fptr(4))
sys.exit(4)



###########################################################3
    
    
eqstr="5*cos(4+4)/arctan(4*5)^((2+5)+2)>6"
funcname2func_dict=get_funcname2func_dict()
funcname2func_dict["+"]=operator.add
funcname2func_dict["-"]=operator.sub
funcname2func_dict["*"]=operator.mul
funcname2func_dict["/"]=operator.truediv
funcname2func_dict["^"]=operator.pow
funcname2func_dict["<"]=operator.lt
funcname2func_dict[">"]=operator.gt


tokens =mtok(eqstr)
stack = []
branch = [] 
args=[]
for tok in tokens:
    toktype=gettoktype(tok)
    if (toktype=="num"):
        branch.append(tok)
    elif (toktype=="operator"):
        branch.append(tok)
    elif (toktype=="var"):
        args.append(tok)
        branch.append(tok)
    elif(toktype=="func"):
        branch.append(tok)
        stack.append(branch)
        branch=[]
    elif(toktype=="oparen"):
        stack.append(branch)
        branch=[]
    elif(toktype=="cparen"):
        r = str2func(branch)
        branch=stack.pop()
        branch.append(r) 
    print "t", tok
    print "tt", toktype
    print "b", branch
    print "s", stack

        
print stack

