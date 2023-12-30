import random
import numpy as np
from numpy import log,exp
import matplotlib.pyplot as plt

T=15
t=np.arange(0,T,0.01)
dt=t[1]-t[0]
n=len(t)

s=0.1
x=np.zeros(8000000)
m=len(x)
td=np.zeros(m)

for i in range(m):
	td[i]=random.gauss(1,s)

count=1
x[0]=0.01

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
string="Number of cells : "+str(count)
plt.hist(x,bins=C,density=True,label=string)

def f(x):
	return 2*log(2)*(2**(-x))

plt.plot(C,f(C),'r-',label='Theoretical Prediction')

plt.xlabel("Cell Age (in units of Division Times)")
plt.ylabel("Probability Density")
string="Normallized Probability Distribution (after "+str(T)+" division times)"
plt.title(string)
plt.legend()
plt.show()

