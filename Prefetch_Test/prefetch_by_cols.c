#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#ifdef ENABLE_prefetch
#define __builtin_prefetch(x, rw, locality)
#endif

#define ROWS 100000
#define COLS 10000

int matrix[ROWS][COLS];

int main(){

    int i, j;

    for (i = 0; i < ROWS;i++){
        for (j = 0; j < COLS;j++){
            matrix[i][j] = rand();
        }
    }

    //get the sum of all elements in matrix
    int64_t sum = 0;
    for (j = 0; j < COLS;j++){
        for (i = 0; i < ROWS;i++){
            sum+= matrix[i][j];
            if(i+1<ROWS-1){
            __builtin_prefetch(&matrix[i+1][j], 0, 3);
            }
        }
    }
    printf("sum = %ld\n", sum);
    return 0;
}