#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


int **constructMatrix(int row, int col){
    int **matrix = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < row;i++){
        matrix[i] = (int *)malloc(sizeof(int) * col);
    }
    return matrix;
}

int main(int argc, char *argv[]){
    int A_row = atoi(*(argv + 1));
    int A_col = atoi(*(argv + 2));
    int B_row = atoi(*(argv + 3));
    int B_col = atoi(*(argv + 4));
    FILE *outputfile;
    outputfile = fopen("matrix", "w");

    //start output matrix A
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j < A_col;j++){
            fprintf(outputfile, "%2d", rand()%100);
            if(j!=A_col-1)
                fprintf(outputfile, " ");
        }
        fprintf(outputfile, "\n");
    }
    fprintf(outputfile, "\n");

    //start output matrix B
    for (int i = 0; i < B_row;i++){
        for (int j = 0; j < B_col;j++){
            fprintf(outputfile, "%2d", rand()%100);
            if(j!=B_col-1)
                fprintf(outputfile, " ");
        }
        if(i!=B_row-1)
            fprintf(outputfile, "\n");
    }

    //close the file
    fclose(outputfile);


    //generate golden answer through ijk method
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
    
    //multiply:
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j <B_col;j++){
            int sum = 0;
            for (int k = 0; k < A_col;k++){
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }

    FILE *golden = fopen("golden", "w");
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j < B_col;j++){
            fprintf(golden, "%d ", C[i][j]);
        }
        fprintf(golden, "\n");
    }
    fprintf(golden, "\n");
    fclose(golden);
    return 0;
}