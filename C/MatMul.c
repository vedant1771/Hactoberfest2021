//Matrix multiplication of sufficiently big size matrices using mutli threading

#include<stdio.h>
#include <unistd.h>
#include<pthread.h>
#include<stdlib.h>


#define MAX_SIZE 1024

long int MatA[MAX_SIZE][MAX_SIZE], MatB[MAX_SIZE][MAX_SIZE], result[MAX_SIZE][MAX_SIZE];
int i,j,k, num_threads;
int step_i = 0;

void* multi(void* arg) {
        int core = step_i++;
        for(int i = core * MAX_SIZE/num_threads; i < (core + 1) * MAX_SIZE / num_threads; i++)
                for (int j = 0; j < MAX_SIZE; j++)
                        for (int k = 0; k < MAX_SIZE; k++)
                                result[i][j] += MatA[i][k] * MatB[k][j];
}


int main(int args, char *argv[]){
	if(args < 2){
		printf("Enter the correct arguments !\n");
		exit(1);
	}
	num_threads = atoi(argv[1]);
	printf("No of Threads : %d\n", num_threads);
	
	for(i = 0; i < MAX_SIZE; i++){
		for(j = 0; j < MAX_SIZE; j++){
			MatA[i][j] = i + j;
			MatB[i][j] = i - j;
		}
	}
	pthread_t threads[num_threads];

        for(int i = 0; i < num_threads; i++){
                int* p;
                pthread_create(&threads[i], NULL, multi, (void*)(p));
        }

        for (int i = 0; i < num_threads; i++) {
           pthread_join(threads[i], NULL);
	}
		
	return 0;
}
