#!/usr/bin/python3

import copy
d = {'A':{1:2}, 'B':{3:4}, 'C':{5:6}}
shallow_copy = copy.copy(d)
deep_copy = copy.deepcopy(d)
d['A'][8] = 9

print("d =", d)
print("shallow_copy = ", shallow_copy)
print("deep_copy = ", deep_copy)
