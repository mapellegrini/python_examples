#!/usr/bin/python

import functools 

lst1=[1, 2, 3, 4]
lst2=[40, 30, 20, 10]

print "lst1=", lst1
print "lst2=", lst2 

strlst=map(str, lst1)
print "strlst = map(str, lst1) = ", strlst

jn=' '.join(strlst) 
print "' '.join(strlst)=", jn

zp=zip(lst1, lst2, strlst)
print "zp= zip(lst1, lst2, strlst) =", zp

zp.sort(key=lambda x:x[1])
print "zp.sort(key=lambda x:x[1])=", zp

lst3=range(5, -5, -1)
print "lst3=", lst3

negs=filter(lambda x: x<0, lst3)
print "filter(lambda x: x<0, lst3)=", negs

product=reduce ((lambda x, y: x*y), lst1)
print "reduce ((lambda x, y: x*y), lst1)=", product

def printlist(start, end, quitval):
  for a in range (start, end):
    print a,
    if (a==quitval):
      print "quit"
      break
  else:
    print "Reached the end of the list"

printlist(0, 10, 5)
printlist(0, 10, 11)

printlist_partialfunc=functools.partial(printlist, 0, 10)
printlist_partialfunc(5)
printlist_partialfunc(11)
