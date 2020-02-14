#!/usr/bin/python -B

from math import sqrt
from math_parse import eqstr2func
from numpy import arange
import argparse

def piover4(x):
  return sqrt(1-x*x)

def simpson(func, start, end, steps):
  width = (end-start) / steps
  xvals = arange(start, end, width)
  area = 0.0  
  for a in range (0, steps-1):
    area +=  width * (func(xvals[a]) + func(xvals[a+1]))/2 
  return area 

parser = argparse.ArgumentParser(description='Calculate the integral of a function using Simpson\'s method')
parser.add_argument('-s', type=float, required=False, default=0.0, help="The starting value for the definite integral. If none is given, will default to 0.0")
parser.add_argument('-e', type=float, required=False, default=1.0, help="The ending value for the definte intgral. If none is given, will default to 1.0")
parser.add_argument('-n', type=int, required=False, default=10, help="Number of steps to use. If none is given, will default to 10")
parser.add_argument('-f', required=False, default="", help="The function to integrate. (Must contain exactly one variable.) If none is given, will default to sqrt(1-x*x), which if integrated from 0 to 1 will give pi/4")
args = parser.parse_args()

if (args.f == ""):
  func = piover4
else:
  func = eqstr2func(args.f)

val = simpson(func, args.s, args.e, args.n) 
print val 



