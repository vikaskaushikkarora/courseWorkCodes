#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#define M_PI 3.14159265358979323846

// Convolution
float convolution(float (*func1)(float), float (*func2)(float), float initial, float final, int n, float t){
	float I=0,x=initial;
	float h=(final-initial)/n;
	for(int i=0;i<n;i++){
		I=I+h*func1(x)*func2(t-x);
		x=x+h;
	}
	return I;
}

// Creating a histogram for age and size distributions
void hist(float *bin, int sizeBin, float *input, int sizeInput, float *output){
	int temp, tempInt, net=0;
	float  h = bin[1]-bin[0], hInv = 1/h;
	
	for(int i=0;i<sizeBin;i++){
		output[i]=0;
	}
	
	for(int j=0;j<sizeInput;j++){
		temp=((hInv*input[j])+0.001);
		tempInt=temp-(bin[0]/h);
		printf("%f\t%d\t%d\n",input[j],temp,tempInt);
		if(tempInt>=0 && tempInt<sizeBin){
			net++;
			output[tempInt] += 1;
		}
	}
	
	//Normallising the histogram
	for(int i=0;i<sizeBin;i++){
		output[i] /= (net*h);
	}
}
