#!/usr/bin/python

import functools 

lst1=[1, 2, 3, 4]
lst2=[40, 30, 20, 10]

print "lst1=", lst1
print "lst2=", lst2 

#mapping a function to a list
strlst=map(str, lst1)
print "strlst = map(str, lst1) = ", strlst

#joining a list into a string using a seperator 
jn=' '.join(strlst) 
print "' '.join(strlst)=", jn

#zipping two lists together 
zp=zip(lst1, lst2, strlst)
print "zp= zip(lst1, lst2, strlst) =", zp

zp.sort(key=lambda x:x[1])
print "zp.sort(key=lambda x:x[1])=", zp

lst3=range(5, -5, -1)
print "lst3=", lst3

#lambda 
negs=filter(lambda x: x<0, lst3)
print "filter(lambda x: x<0, lst3)=", negs

#reduce 
product=reduce ((lambda x, y: x*y), lst1)
print "reduce ((lambda x, y: x*y), lst1)=", product

#for-else example 
#while-else is also legal 
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
#defines a partial function identical to printlist, except the first argument is pegged
#to 0 and the second argument is pegged to 10 

printlist_partialfunc(5)
printlist_partialfunc(11)

#try-except-else 
try:
  print "Executing try statement : ",
except:
  print "Whoops, something went wrong" 
else:
  print "Nothing went wrong"