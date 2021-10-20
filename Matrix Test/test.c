#include <stdio.h>
#include <stdlib.h>

#define row 1024
#define col 1024

int **ConstructMatrix(){
    int **matrix = NULL;
    matrix = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < col;i++){
        matrix[i] = (int *)malloc(sizeof(int) * col);
    }

    return matrix;
}

int main(){



}