import os
os.system("rm lcpfct.pyf")
os.system("rm lcpfct.cpython-311-x86_64-linux-gnu.so")
os.system("python3 -m numpy.f2py lcpfct.f -m lcpfct -h lcpfct.pyf")
os.system("python3 -m numpy.f2py -c lcpfct.pyf lcpfct.f")

import numpy as np
import matplotlib.pyplot as plt
import lcpfct as lp

nx = 1000
L = 35.00
dx = L/nx
timesteps = 4000
iprint = 25
dt = 0.01
u = 0.500

amp = 0.1
x_int = dx*np.arange(nx+1,dtype='f')
xMid = np.zeros(nx,dtype='f')
rho = np.zeros(nx,dtype='f')
v_int =np.zeros(nx+1,dtype='f')

for i in range(0,nx):
    xMid[i] = (2*i - 1)*0.5*dx

for i in range(0,nx):    
	rho[i] = amp*np.exp(-((xMid[i]-10.0)/2.00)**2)

for i in range(1,nx):
	v_int[i] = (rho[i-1]+rho[i])/2
v_int[0]=(rho[0]+rho[nx-1])/2
v_int[nx]=(rho[0]+rho[nx-1])/2

plt.plot(xMid,rho,'r')
#lp.residiff(1.00000)
#lp.residiff(1.00)
lp.makegrid(x_int,x_int,1,1)
lp.velocity(v_int,0,dt)

#plt.plot(xMid,rho)

rho_out = np.zeros(nx)
time = 0.0

for i in range(timesteps):
	#rho_out = lp.lcpfct(rho,0,nx-1,0.0,0.0,0.0,0.0,1)
	
	half = [1,2]
	#print(i)
	for j in half:
		dtstep = 0.5*j*dt
		lp.velocity(v_int,0,dtstep)
		rho_out = lp.lcpfct(rho,0,nx,0.0,0.0,0.0,0.0,1)
		
	#print(np.shape(rho))
	rho[:] = rho_out[:]
	for k in range(1,nx):
		v_int[k] = (rho[k-1]+rho[k])/2
	v_int[0]=(rho[0]+rho[nx-1])/2
	v_int[nx]=(rho[0]+rho[nx-1])/2
	
	if (i%200 == 0):
		plt.plot(xMid,rho,'g-',linewidth=0.4) 
	time = time + dt
	
   #for ii in range(0,nx):
    #rho[ii] = rho_out[ii]

#print(type(rho))
plt.show()

