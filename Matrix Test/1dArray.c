#include <stdio.h>
#include <stdlib.h>

typedef struct _matrix{
    int row;
    int col;
    int *value;
} matrix;

void initMatrix(matrix *A){
    A->value = malloc(sizeof(int) * A->row * A->col);
}

void freeMatrix(matrix *A){
    free(A->value);
}

void readfile(matrix *A, matrix *B){
    FILE *input = fopen("matrix", "r");
    for (int i = 0; i < A->row * A->col;i++){
        fscanf(input, "%d", &(A->value[i]));
    }
    for (int i = 0; i < B->row * B->col;i++){
        fscanf(input, "%d", &(B->value[i]));
    }
    fclose(input);
}

void printMatrix(matrix A){
    for (int count = 0; count < A.row * A.col;count++){
        printf("%d ", A.value[count]);
        if((count+1)%A.col==0)
            printf("\n");
    }
}

int main(int argc, char *argv[]){

    matrix A;
    matrix B;
    A.row = atoi(*(argv + 1));
    A.col = atoi(*(argv + 2));
    B.row = atoi(*(argv + 3));
    B.col = atoi(*(argv + 4));

    initMatrix(&A);
    initMatrix(&B);

    readfile(&A, &B);
    printMatrix(A);
    printMatrix(B);
    //freeMatrix(A.value);
    //freeMatrix(B.value);
    return 0;
}