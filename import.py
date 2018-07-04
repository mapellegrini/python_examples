#!/usr/bin/python -B
#use the -B option to prevent the creation of .pyc files

print "Importing concurrency" 
import concurrency
#import brings in everything that's not wrapped in "if __name__ == '__main__':"

print "Importing getstdout" 
from getstdout import getstdout
#there's nothing in getstdout.py other than imports and function definitions
#this is how a module should be written

print "Importing complex"
import complex as modulename 
#executes all non-definitional code in circle.py 
#modes should avoid doing this


print "\n\n\nFinished importing. Now using those imports." 
c1=modulename.complex(1,2)

mylst=[] 
concurrency.thread_func(mylst, c1, "teststr") #one line function: arg1.append(str(arg2) + arg3)
print mylst #mylst was modified during the call to thread_func
