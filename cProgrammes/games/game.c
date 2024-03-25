#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<unistd.h>

#define timeSteps 2000
char playerName[10];

int main(){
	/*
	printf("Please Enter the player\'s name : ");
	scanf("%s",&playerName);
	printf("Welcome Mr./Ms. %s , Let\'s play this game : \n",playerName);
	printf("You can quit anytime by pressing Control+D\n");
	sleep(2);
	*/
	while(1){
		for(int i=0;i<50;i++){
			for(int j=0;j<50;j++){
				printf(" ");
			}
			printf("\n");
		}
		for(int i=0;i<50;i++){
			printf("=");
		}
		printf("\n");
		sleep(0.5);
		system("clear");
	}
	return 0;
}
