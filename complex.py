#!/usr/bin/python
#This script contains the implementation of a python class for complex
#numbers in order to demonstrate how to do operator overloading with classes
#This is a fantastic tutorial that explains how to do it:
#http://thepythonguru.com/python-operator-overloading/

import math 

class complex:
  def __init__(self, real, comp):
    self.__real = real
    self.__comp = comp

  def getreal(self):
    return self.__real

  def getcomp(self):
    return self.__comp

  def __add__(self, other):
    return complex(self.getreal() + other.getreal(), self.getcomp()+other.getcomp())

  def __sub__(self, other):
    return complex(self.getreal() - other.getreal(), self.getcomp() - other.getcomp())
  
  def __mul__(self, other):
    r = self.getreal() * other.getreal() - self.getcomp() * other.getcomp()
    c = self.getreal() * other.getcomp() + self.getcomp() * other.getcomp()
    return complex(r,c)

  def getboth(self):
    return [self.getreal(), self.getcomp()]

  def __str__(self):
    return str(self.getreal()) + "+" + str(self.getcomp()) + "i"

  def magnitude(self):
    r = self.getreal()
    i = self.getcomp()
    return math.sqrt(r*r+i*i)

  def __lt__ (self, another_complex):
    if (self.magnitude() < another_complex.magnitude()):
      return True
    return False

  

x1=complex(1,2)
x2=complex(3,4)
x3=complex(5,6)
x4=complex(7,8)
x5=complex(0,0)

print (x1 + x2)
print (x3 - x1)
print (x2 * x3)

print x3*x3*x3*x3*x3*x3
print "\n\n"


print "List sorting:"
lst = [x5, x4, x3, x2, x1]
for a in lst:
  print a, 
print ""
lst.sort()
for a in lst:
  print a, 
print ""


def julia(r, comp, c, n):
  z = complex(r, comp)
  cit = complex(c,0) 
  cur = z 

  for a in range (0,  n):
    cur = cur * z + cit 
    print cur

print "\n\nJulia sets:"
julia(0.5, 0.6, 0.3, 10)
  
  
