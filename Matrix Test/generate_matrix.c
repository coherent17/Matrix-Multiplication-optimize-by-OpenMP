#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]){
    int row = atoi(*(argv + 1));
    int col = atoi(*(argv + 2));
    FILE *outputfile;
    outputfile = fopen("matrix", "w");

    //start output
    for (int i = 0; i < row;i++){
        for (int j = 0; j < col;j++){
            fprintf(outputfile, "%2d ", rand()%100);
        }
        fprintf(outputfile, "\n");
    }
    fprintf(outputfile, "\n");
    fclose(outputfile);
    return 0;
}