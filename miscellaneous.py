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

mysumfunc=functools.partial(reduce, (lambda x,y: x+y)) #defining a partial function which sums a given list
print "mysumfunc(lst1)=", mysumfunc(lst1)


