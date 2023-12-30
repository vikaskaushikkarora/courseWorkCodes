import os
import random
import numpy as np
from numpy import log,exp
import matplotlib.pyplot as plt

os.system("rm -r /home/vikas/Desktop/work/images")
os.system("mkdir /home/vikas/Desktop/work/images")

T=25
t=np.arange(0,T,0.01)
dt=t[1]-t[0]
n=len(t)

s=0.1
x=np.zeros(30000000)
m=len(x)
td=np.zeros(m)

for i in range(m):
	td[i]=random.gauss(1,s)

count=1
x[0]=0.01

def f(x):
	return 2*log(2)*(2**(-x))

for i in range(n-1): #loop for time
	for j in range(count): #for all cells at that time
		if (x[j]>=td[j]):
			x[j]=0.01
			x[count]=0.01
			count=count+1
			td[j]=random.gauss(1,s)
		else :
			x[j]=x[j]+dt
	
	C=np.arange(0.01,2,0.02)
	plt.hist(x,bins=C,density=True)
	plt.plot(C,f(C),'r-',label='Theoretical Prediction')
	plt.plot([1,1],[0,2],'k-',linewidth=0.3,label='Division Time')
	plt.xlabel("Cell Age (in units of Division Times)")
	plt.ylabel("Probability Density")
	plt.ylim(0,2)
	string="Time : "+str(round(t[i],2))
	plt.text(1.5,1.5,string)
	string="Number of Cells: "+str(count)
	plt.title(string)
	string="/home/vikas/Desktop/work/images/fig"+str(i)+".png"
	plt.legend()
	plt.savefig(string,dpi=300)
	plt.clf()

string="ffmpeg -framerate 30 -i /home/vikas/Desktop/work/images/fig%d.png -c:v libx264 -vf format=yuv420p /home/vikas/Desktop/work/output.mp4"
os.system(string)
