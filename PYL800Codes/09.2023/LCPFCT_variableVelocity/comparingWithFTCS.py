import numpy as np
from numpy import pi,exp,sqrt
import matplotlib.pyplot as plt

t=np.arange(0,40,0.01)
n=len(t)
x=np.linspace(0,35,1000)

n=len(t)
m=len(x)
dt=t[1]-t[0]
dx=x[1]-x[0]

u=np.zeros((n,m),dtype=float)

#initial condition
u[0,:]=(0.1)*exp(-((x-10)**2)/(4))
#boundary condition
u[:,0]=0
u[:,m-1]=0

for i in range(n-1):
	for j in range(1,m-1):
		u[i+1,j]=u[i,j]-0.5*(dt/dx)*u[i,j]*(u[i,j+1]-u[i,j-1])

s=25
for i in range(int(n/s)):
	plt.plot(x,u[s*i,:],'r-')
	plt.xlim(0,35)
	plt.ylim(0,0.15)
	plt.grid()
	plt.pause(0.01)
	plt.clf()

plt.show()
