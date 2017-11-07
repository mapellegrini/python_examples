#!/usr/bin/python

class Circle:
 
    def __init__(self, radius):
        self.__radius = radius
 
    def setRadius(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def area(self):
        return math.pi * self.__radius ** 2
 
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )

    def __lt__ (self, another_circle):
      if (self.__radius < another_circle.__radius ):
        return True 
      return False


c1 = Circle(4)
c2 = Circle(5)
c3 = Circle(6)
c4 = Circle(7)

lst = [c4, c3, c2, c1]
print "Unsorted"
for c in lst:
  print c.getRadius()

  
lst.sort()
print "\n\nSorted"
for c in lst:
  print c.getRadius()

