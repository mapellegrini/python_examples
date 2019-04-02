#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Compare two files and print the difference in red')
parser.add_argument('-o', required=True, help="Old text file")
parser.add_argument('-n', required=True, help="New text file")
args = parser.parse_args()

redfg='\033[31m'
redbg='\033[41m'
reset='\033[0m'


f=file(args.o)
oldtext=f.read()
f.close()

f=file(args.n)
newtext=f.read()
f.close()

olines=oldtext.split("\n")
nlines=newtext.split("\n")

for [oldline, newline] in zip(olines, nlines):
  pline = ""
  ochars=list(oldline)
  nchars=list(newline)  
  m = min(len(ochars), len(nchars))
  
  if (len(ochars) < len(nchars)):
    newbigger=True
  else:
    newbigger=False
  for a in range(0, m):
    if (ochars[a]==nchars[a]):
      pline += ochars[a]
    else:
      pline += redfg + nchars[a] + reset
  if (newbigger):
    pline+= redfg + "".join(nchars[m:]) + reset
  else:
    pline+=redbg + "".join(ochars[m:]) + reset
  print pline







  
