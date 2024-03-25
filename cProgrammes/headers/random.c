#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#define M_PI 3.14159265358979323846

//-----------------SINGLE RANDOM NUMBER---------------------

//Unifrom Interger in a range 
int rI(int lowerLimit, int upperLimit){
	int a = lowerLimit + (rand()%(upperLimit-lowerLimit+1));
	return a;
}

//Unifrom Float in a range
float rU(int lowerLimit, int upperLimit){
	float a = lowerLimit + (upperLimit-lowerLimit)*(rand()*pow(RAND_MAX,-1));
	return a; 
}

//Gaussian Float
float rG(float mu, float s){
	float u = (rand())*pow(RAND_MAX,-1);
	float v = (rand())*pow(RAND_MAX,-1);
	float x = s*(sqrt(-2*log(u))*sin(2*M_PI*v))+mu;
	return x;
}

//Exponential Float
float rE(float lambda){
	float a;
	a=rand()/(RAND_MAX +1.0);
	return -log(1-a)/lambda;
}

//-------------------A RANDOM ARRAY-------------------------------
//We create a function returning a pointer to the required array containing random number

//Guassian Float Array (Gives a random number array with gaussian pdf)
float* randomGaussian(int n,float mu, float s){ //s=standard deviation and mu=average
	float* u = malloc(n* sizeof(float));
	float* v = malloc(n* sizeof(float));
	float* x = malloc(n* sizeof(float));
	
	for(int i=0;i<n;i++){
		u[i]=(rand())*pow(RAND_MAX,-1);
		v[i]=(rand())*pow(RAND_MAX,-1);
		x[i]=s*(sqrt(-2*log(u[i]))*sin(2*M_PI*v[i]))+mu;
	}
	return x;
}

//Exponential Float Array (Gives a random number array with exponential decaying pdf)
float* randomExponential(int n, float lambda){
	float* temp = malloc(n*sizeof(float));
	float* x = malloc(n*sizeof(float));
	for(int i=0;i<n;i++){
		temp[i]=rand()/(RAND_MAX +1.0);
		x[i]=-log(1-temp[i])/lambda;
	}
	return x;
}
