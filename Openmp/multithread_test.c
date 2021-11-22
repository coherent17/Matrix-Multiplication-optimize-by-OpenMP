#include <stdio.h>
#include <omp.h>

int main(){
    printf("I am master thread!\n");

    #pragma omp parallel
    {
        printf("I am multithread!\n");
    }
    return 0;
}