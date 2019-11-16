#!/usr/bin/python

import numpy 
import argparse
import math

def piover4(x):
  return math.sqrt(1-x*x)

def simpson(func, start, end, steps):
  width = (end-start) / steps
  xvals = numpy.arange(start, end, width)
  area = 0.0  
  for a in range (0, steps-1):
    area +=  width * (func(xvals[a]) + func(xvals[a+1]))/2 
  return area 

parser = argparse.ArgumentParser(description='Calculate pi using Simpson\'s method')
parser.add_argument('-n', type=int, required=False, default=10, help="Number of steps to use")
args = parser.parse_args()

pi = 4.0 * simpson(piover4, 0.0, 1.0, args.n)
print "Pi = ", pi


