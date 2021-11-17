#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define ROWS 100000
#define COLS 10000

int matrix[ROWS][COLS];

int main(){

    int i, j;

    //put something into matrix
    for (i = 0; i < ROWS;i++){
        for (j = 0; j < COLS;j++){
            matrix[i][j] = rand();
        }
    }

    //get the sum of all elements in matrix
    int64_t sum = 0;
    for (i = 0; i < ROWS;i++){
        for (j = 0; j < COLS;j++){
            sum+= matrix[i][j];
            //builtin_prefetch:
            if(j+1<COLS && ((j+1)-1)%8==0){
                __builtin_prefetch(&matrix[i][j+1], 0, 3);
            }
        }
        if(i+1<ROWS){
            __builtin_prefetch(&matrix[i+1][j], 0, 3);
        }
    }
    printf("sum = %ld\n", sum);
    return 0;
}