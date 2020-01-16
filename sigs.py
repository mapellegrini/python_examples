#!/usr/bin/python

import atexit
import signal
import sys
import os 

def exithandler(*args): #exit handler
  print "Recieved an exit"
  for arg in args:  
    print (arg) 
  sys.exit(0)
    
def sighandler(*args): #all-purpose signal handler 
  print "Recieved a signal"
  for arg in args:  
      print (arg) 
  sys.exit(0)

#register the functions
atexit.register(exithandler)  

for sig in (signal.SIGABRT, signal.SIGILL, signal.SIGINT, signal.SIGSEGV, signal.SIGTERM):
  signal.signal(sig, sighandler)

mypid=os.getpid()

  
while (True):
  print "Enter a signal number, or -1 to exit"

  val = int(input())
  if (val == -1):
    break
  else:
    os.kill(mypid, val)
  
