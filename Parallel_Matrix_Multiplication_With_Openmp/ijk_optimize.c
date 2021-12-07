#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <omp.h>

#define Start(X) double X = omp_get_wtime()
#define Stop(X) printf("%s: %g sec.\n", (#X), (double)(omp_get_wtime() - (X)))

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

int main(int argc, char *argv[]){

    A_row = atoi(*(argv + 1));
    A_col = atoi(*(argv + 2));
    B_row = atoi(*(argv + 3));
    B_col = atoi(*(argv + 4));
    int number_of_threads = atoi(*(argv + 5));

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

    fclose(input);

    Start(ijk_optimize_runtime);
    //multiply:
    int i, j, k;
    #pragma omp parallel shared(A,B,C) private(i,j,k) num_threads(number_of_threads)
    {   
        #pragma omp for
            for (i = 0; i < A_row;i++){
                for (j = 0; j <B_col;j++){
                    int sum = 0;
                    for (k = 0; k < A_col;k++){
                        sum += A[i][k] * B[k][j];
                    }
                    C[i][j] = sum;
                }
            }
    }
    Stop(ijk_optimize_runtime);

    //output the result to compare with golden result
    FILE *out = fopen("ijk_optimize_result", "w");
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j < B_col;j++){
            fprintf(out, "%d ", C[i][j]);
        }
        fprintf(out, "\n");
    }
    fprintf(out, "\n");
    fclose(out);
    return 0;
}