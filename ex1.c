/*Project Euler 1 in c*/
#include <stdio.h>

int main(){
	printf("Sum: %i\n", run(1000));
	return 0;
}
int run(int limit){
	int x;
	int sum =0;
	for(x=1; x<limit; x++){
		if(x%3==0){
			sum=sum+x;
			continue;
		}
		if(x%5==0){
			sum=sum+x;
			continue;
		}
		}
		return sum;
		}