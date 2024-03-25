#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#define M_PI 3.14159265358979323846

//Differentiation
float diff(float (*func)(float), float x, float h){
	float D=(func(x+h)-func(x))/h;
	return D; 
}

//Integration
float intg(float (*func)(float), float initial, float final, int n){
	float I=0,x=initial;
	float h=(final-initial)/n;
	for(int i=0;i<n;i++){
		I=I+h*func(x);
		x=x+h;
	}
	return I;
}

