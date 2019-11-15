#!/usr/bin/python

from collections import defaultdict

dd1 = defaultdict(list)
dd2 = defaultdict(str) 
dd3 = defaultdict((lambda: "Default string"))
dd4 = defaultdict((lambda: 1))

print dd1[10]
print dd2[10]
print dd3[10]
print dd4[10]
