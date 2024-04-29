# Random Walk with Absorbing Boundary Condition : Animation

import numpy as np
import matplotlib.pyplot as plt

A=np.loadtxt("/home/vikas/work/data.txt") #load the data
n=len(A[:,0])
C=np.linspace(-200,50,250) # bin for histogram

# Animation
s=5 # speed of the animation
for i in range(int(n/s)):
	plt.hist(A[s*i,:],bins=C,density=True)
	plt.grid()
	#plt.ylim(-0.01,0.15)
	string="Absorbing Boundary Conditions Random Walk at time = "+str(round((s*i*0.01),2))
	plt.title(string)
	plt.pause(0.1)
	plt.clf()
	
plt.show()
#plt.savefig("/sdcard/Pictures/plot.png",dpi=300)
