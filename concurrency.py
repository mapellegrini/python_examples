#!/usr/bin/python

#Shows how to execut multiple concurrent threads using python's shared memory concurrency library
#Demonstrates how to pass messages (lists) using the manager construct

import multiprocessing 

def thread_func(manager, threadnum, mystr):
  manager.append(str(threadnum) + mystr)

if __name__ == '__main__':
  numthreads = 10
  #manager = multiprocessing.Manager() 
  manager = multiprocessing.Manager().list() 
  threads=[]

  for w in range(numthreads):
    threads.append(multiprocessing.Process(target=thread_func, args=(manager, w, "randstr")))

  for w in range(numthreads):
    threads[w].start()

  for w in range(numthreads):
    threads[w].join()

  manager.sort()
  print manager
