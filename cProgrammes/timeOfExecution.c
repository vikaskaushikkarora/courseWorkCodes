#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#define sizeArr 1e9

int main(int argc,char* argv[]){
	clock_t thisTime = clock();
	
	// Block of Code ==================================================
	int *arr = malloc(sizeArr*sizeof(int));
	for(int i=0;i<sizeArr;i++){
		arr[i]=i;
	}
	//=================================================================
	
	thisTime = clock()-thisTime;
	double timeTaken = (double)thisTime/CLOCKS_PER_SEC;
	printf("Time taken for execution : %lf seconds\n",timeTaken);
	return 0;
}
