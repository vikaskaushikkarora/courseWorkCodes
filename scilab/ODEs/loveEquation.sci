// Clear console and figure
clc
clf
funcprot(0)

//Define Constants
a=1
b=0.5
c=1
d=0.5

e=1
f=0.5
g=1
h=0.5

//Initial values of love of y for z and love of z for y
y=1
z=1

//Intial Time
t0=0.01 

//Define the ODE for dynamics of love
function dx=f(t,x)
	dx(1)=a*x(1)+(c-(b/(x(1)+d)))*x(2);
	// a : Ek tarfa pyar wala constant for lover y
	dx(2)=e*x(2)+(g-(f/(x(2)+h)))*x(1);
	// e : Ek tarfa pyar wala constant for lover z
endfunction

//Solve ODE and plot the values of love vs time
sol=ode([y,z]',t0,t,f)
t=0.01:0.01:10
plot(t,sol(1))
