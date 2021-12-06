#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>

#define Start(X) clock_t X = clock()
#define Stop(X) printf("%s: %g sec.\n", (#X), (double)(clock() - (X)) / CLOCKS_PER_SEC)

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

double omp_get_wtime(void);

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

    fclose(input);

    double start = omp_get_wtime();
    //multiply:
    int i, j, k;
    #pragma omp parallel shared(A,B,C) private(i,j,k)
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
    double stop = omp_get_wtime();
    printf("ijk_optimize runtime %f sec.\n", stop - start);

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