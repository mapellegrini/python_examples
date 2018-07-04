#!/usr/bin/python

import subprocess

def getstdout(command, inc_stderr=False):
  #print "executing:", command
  if (inc_stderr):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
  else:
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
  output = proc.stdout.read()
  return output.lstrip().rstrip()


