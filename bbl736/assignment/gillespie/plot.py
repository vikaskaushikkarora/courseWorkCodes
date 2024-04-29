# Plotting the graph

import numpy as np
import matplotlib.pyplot as plt

# Importing the required data
D=np.loadtxt("/home/vikas/work/data.txt")
D1=np.loadtxt("/home/vikas/work/data1.txt")

# Plot all ensembles
n=int(0.5*len(D1[0,:]))
for i in range(n):
	t1=D1[:,2*i]
	P1=D1[:,2*i+1]
	plt.plot(t1,P1,linewidth=1)

# Plot the average ensemble
t=D[:,0]
P=D[:,1]
#plt.plot(t,P,'k-*',markersize=1,label="Average Behaviour")

# Annotate the graph
plt.xlabel("Time")
plt.ylabel("Number of P Molecules")
plt.grid()
plt.title("Autoactivator Genetic Circuit Using Gillespie Algorithm")
# Show the graph
#plt.show()
plt.savefig("plot.png",dpi=500)
