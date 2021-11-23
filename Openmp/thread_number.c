#include <stdio.h>
#include <omp.h>

int main(){
    #pragma omp parallel num_threads(4)
    {
        int ID = omp_get_thread_num();
        printf("Thread number =  %d\n", ID);
    }

    printf("----------------------------\n");

    omp_set_num_threads(3);
    #pragma omp parallel
    {
        int ID = omp_get_thread_num();
        printf("Thread number =  %d\n", ID);
    }
    return 0;
}