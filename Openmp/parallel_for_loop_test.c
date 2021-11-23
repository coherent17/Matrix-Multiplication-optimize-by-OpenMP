#include <stdio.h>
#include <omp.h>

int main(){
    #pragma omp parallel num_threads(4)
    {
        #pragma omp for
        for (int i = 0; i < 12;i++){
            int ID = omp_get_thread_num();
            printf("CPU<%d>: %d\n",ID, i);
        }
    }

    printf("-------------------\n");

    omp_set_num_threads(4);
    #pragma omp parallel for
    for (int i = 0; i < 12;i++){
        int ID = omp_get_thread_num();
        printf("CPU<%d>: %d\n",ID, i);
    }
    printf("\n");
    return 0;
}