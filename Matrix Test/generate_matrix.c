#include <stdio.h>
#include <stdlib.h>

#define row 10
#define col 10

int main(){
    FILE *outputfile;
    outputfile = fopen("matrix", "w");

    //start output
    for (int i = 0; i < row;i++){
        for (int j = 0; j < col;j++){
            fprintf(outputfile, "%2d ", rand()%100+10);
        }
        fprintf(outputfile, "\n");
    }
    fprintf(outputfile, "\n");
    fclose(outputfile);
    return 0;
}