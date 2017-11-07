#!/usr/bin/python

import numpy 
import argparse
import math

def f(x):
  return math.sqrt(1-x*x)

parser = argparse.ArgumentParser(description='Calculate pi using Simpson\'s method')
parser.add_argument('-n', type=int, required=False, default=10, help="Number of steps to use")
args = parser.parse_args()


width = 1.0 / args.n
vals = numpy.arange(0.0, 1.0, width)
area = 0.0 

for a in range (0, len(vals)-1):
  area +=  width * (f(vals[a]) + f(vals[a+1]))/2 
area *= 4 
print "Pi = ", area 
