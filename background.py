#!/usr/bin/python

import os
import sys


def isbackground():
  if (os.getpgrp() == os.tcgetpgrp(sys.stdout.fileno())):
    print "Running in foreground"
  else:
    print "Running in background"

isbackground()
