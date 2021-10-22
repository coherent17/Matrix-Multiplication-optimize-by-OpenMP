#include <stdio.h>
#include <stdlib.h>

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
    return 0;
}