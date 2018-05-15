#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
import random 

xvals=[]
yvals=[]
for a in range (100):
  xvals.append(random.randint(-10, 10))
  yvals.append(random.randint(-10, 10))

matplotlib.rcParams['axes.unicode_minus'] = False #this is the default behavior anyway
fig, ax = plt.subplots()

plt.xlabel("Xvals")
plt.ylabel("Yvals")

plt.xscale("linear") #this is the default behavior anyway
plt.yscale("linear") #this is the default behavior anyway

plt.xlim(-15, 15)
plt.ylim(-15, 15)

#ax.relim()      #uncomment to enable autoscaling
#ax.autoscale()  #uncomment to enable autoscaling

ax.plot(xvals, yvals, 'o')
ax.set_title("This is the title of my graph")
plt.savefig("/tmp/scatter.jpg")

