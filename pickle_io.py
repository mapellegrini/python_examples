#!/usr/bin/python

import pickle

dict1 = {1 : 1, 2: 3, 5 : 6, 9 : 10 }

f = file("/tmp/dict.pickle", "w")
pickle.dump(dict1, f)
f.close()


f = file("/tmp/dict.pickle", "r")
dict2 = pickle.load(f)
f.close()
print dict2 
