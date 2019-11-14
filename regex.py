#!/usr/bin/python

import re
import sys


teststr1 = "Cats are smarter than dogs"
#re.match checks the beginning of the string only
#check it for a match, and break up the result into groups using ()

matchObj = re.match( r'(.*) are (.*?) (.*)', teststr1) 

if matchObj:
   print "teststr0 match() ", matchObj.group()
   print "teststr0 match(0)", matchObj.group(0) #same as ()
   print "teststr0 match(1)", matchObj.group(1)
   print "teststr0 match(2)", matchObj.group(2)
   print "teststr0 match(3)", matchObj.group(3)
   print "\n\n"
else:
   print "No match!!"
   print "\n\n"
   
#re.search searches the whole string for a the first match 

teststr2="Hello my name is Bobby."
m=re.match("name is A[A-z]*", teststr2)
s=re.search("name is [A-z]*", teststr2)

if (m):
  print "teststr1 match", m.group()
if (s):
  print "teststr1 search:", s.group()
print "\n\n"
   
  
teststr3="Going Going03 going99 going104"
#findall matches all results
results=re.findall("going[0-9]*", teststr3, re.M|re.I) 
#re.M means the input is (could be) multi-line
#re.I means ignore case
print results


regex="key"
targetstring1 = "The key is to keyin on keys that keyword keykeykey"
targetstring2 = "The magic phrase does not appear in this string"
pattern = re.compile(regex)
searchfunc1 = pattern.search(targetstring1)
searchfunc2 = pattern.search(targetstring2)


if (searchfunc1 != None): #the pattern exists in the string
   print regex, "was found in target string", targetstring1

if (searchfunc2 == None): #the pattern does not exist in the string
   print regex, "was not found in the targetstring", targetstring2

   
