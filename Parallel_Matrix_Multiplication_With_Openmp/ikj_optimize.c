#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

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

void freeMatrix(int **matrix, int row, int col){
    for (int i = 0; i < row;i++){
        free(matrix[i]);
    }
    free(matrix);
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

    double start_time = omp_get_wtime();
    //multiply:
    int i, j, k;
    int temp;
    #pragma omp parallel for shared(A,B,C) private(i,j,k,temp) num_threads(number_of_threads)  
        for (i = 0; i < A_row;i++){
            for (k = 0; k < B_row;k++){
                temp = A[i][k];
                for (j = 0; j < B_col;j++){
                    C[i][j] += temp * B[k][j];
                }
            }
        }

    double end_time = omp_get_wtime();
    printf("%s: %g sec.\n", "ikj_optimize_runtime", end_time - start_time);

    //output the result to compare with golden result
    FILE *out = fopen("ikj_optimize_result", "w");
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j < B_col;j++){
            fprintf(out, "%d ", C[i][j]);
        }
        fprintf(out, "\n");
    }
    fprintf(out, "\n");
    fclose(out);
    
    freeMatrix(A, A_row, A_col);
    freeMatrix(B, B_row, B_col);
    freeMatrix(C, A_row, B_col);
    return 0;
}