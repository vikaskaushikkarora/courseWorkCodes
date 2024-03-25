#include <stdio.h>
#define IN 0

int main()
{
	short count=0,n=20;
	int len[n],c;
	for(int i=0;i<n;i++){
		len[i]=0;
	}
	while((c=getchar())!=EOF){
		if(c==' ' || c=='\t' || c=='\n'){
			len[count]++;
			count=0;
		}else{
			count++;
		}
	}
	for(int i=0;i<n;i++){
		printf("count[%2d]",i);
		for(int j=0;j<len[i];j++){
			printf("=");
		}
		printf("\n");
	}
	return 0;
}

