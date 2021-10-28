#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int A_row;
int A_col;
int B_row;
int B_col;

int **constructMatrix(int row, int col){
    int **matrix = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < row;i++){
        matrix[i] = (int *)malloc(sizeof(int) * col);
    }
    return matrix;
}

void printMatrix(int **matrix, int row, int col){
    for (int i = 0; i < row;i++){
        for (int j = 0; j < col;j++){
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main(int argc, char *argv[]){

    A_row = atoi(*(argv + 1));
    A_col = atoi(*(argv + 2));
    B_row = atoi(*(argv + 3));
    B_col = atoi(*(argv + 4));

    FILE *input = fopen("matrix", "r");

    int **A = constructMatrix(A_row, A_col);
    int **B = constructMatrix(B_row, B_col);
    int **C = constructMatrix(A_row, B_col);


    //read A
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j < A_col;j++){
            fscanf(input, "%d", &A[i][j]);
        }
    }


    //read B
    for (int i = 0; i < B_row;i++){
        for (int j = 0; j < B_col;j++){
            fscanf(input, "%d", &B[i][j]);
        }
    }

    //multuply:
    for (int i = 0; i < A_row;i++){
        for (int k = 0; k < B_row;k++){
            int temp = A[i][k];
            for (int j = 0; j < B_col;j++){
                C[i][j] += temp * B[k][j];
            }
        }
    }


    //printMatrix(A, A_row, A_col);
    //printMatrix(B, B_row, B_col);
    //printMatrix(C, A_row, B_col);


    fclose(input);
    return 0;
}