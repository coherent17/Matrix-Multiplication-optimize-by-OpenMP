# Matrix Multiplication With Spatial Locality

## Using specific data structure to improve the spatial locality?

*   1D Array: 難追蹤index，且不能改善矩陣列與列間沒辦法達成hit cache的情況
*   2D Array: 雖然列與列之間需要重新load/store，但是index標示方便，因此我後面選擇使用這個來做運算
*   Linkedlist: node與node間很大機率為不連續，因此我認為這個的spatial locality會最差

    假如cache line size = 32bytes = 8 * sizeof(int)，也就是說就算load/store Row-Wise的連續記憶體空間，每8個一循環就會有一次not hit。

## How to change the calculation order to improve the spatial locality?

在使用相同演算法下$O(n^3)$，有兩種方法可以優化spatial locality。
*   1. 在cache line所存放的datatype所佔的空間越小，那麼便可以存放較多的data，因此在同行的hit rate會較高
*   2. 改變算的順序，盡量減少not hit的機率


## Coding Time

### **ijk method & jik method**


![](https://i.imgur.com/xFGSyhd.png)

```c
//ijk_method
for (int i = 0; i < A_row;i++){
    for (int j = 0; j <B_col;j++){
        int sum = 0;
        for (int k = 0; k < A_col;k++){
            sum += A[i][k] * B[k][j];
        }
        C[i][j] = sum;
    }
}
```
```c
//jik_method
for (int j = 0; j < B_col;j++){
    for (int i = 0; i < A_row;i++){
        int sum = 0;
        for (int k = 0; k < A_col;k++){
            sum += A[i][k] * B[k][j];
        }
        C[i][j] = sum;
    }
}
```
因為是使用int的datatype，因此在一個cache line(32 bytes)中最多可以放8個data，對於這兩種方法(ijk_method和jik_method)來算算他們在一個cache line中的not hit rate:  

| method     | A    | B    | C    | total |
| :--------- | :--- | :--- | :--- | :---- |
| ijk method | 1/8  | 8/8  | 0/8  | 1.125 |
| jik method | 8/8  | 1/8  | 0/8  | 1.125 |

### **jki method & kji method**
![](https://i.imgur.com/wKFxaZT.png)


```c
//jki_method
for (int j = 0; j < B_col;j++){
    for (int k = 0; k < A_col;k++){
        int temp = B[k][j];
        for (int i = 0; i < A_row;i++){
            C[i][j] += A[i][k] * temp;
        }
    }
}
```
```c
//kji_method
for (int k = 0; k < A_col;k++){
    for (int j = 0; j < B_col;j++){
        int temp = B[k][j];
        for (int i = 0; i < A_row;i++){
            C[i][j] += A[i][k] * temp;
        }
    }
}
```

一個cache line中的not hit rate:
| method     | A    | B    | C    | total |
| :--------- | :--- | :--- | :--- | :---- |
| jki method | 8/8  | 0/8  | 8/8  | 2     |
| kji method | 8/8  | 0/8  | 8/8  | 2     |

### **kij method & ikj method**
![](https://i.imgur.com/jkYicuO.png)


```c
//kij_method
for (int k = 0; k < A_col;k++){
    for (int i = 0; i < A_row;i++){
        int temp = A[i][k];
        for (int j = 0; j < B_col;j++){
            C[i][j] += temp * B[k][j];
        }
    }
}
```
```c
//ikj_method
for (int i = 0; i < A_row;i++){
    for (int k = 0; k < B_row;k++){
        int temp = A[i][k];
        for (int j = 0; j < B_col;j++){
            C[i][j] += temp * B[k][j];
        }
    }
}
```
一個cache line中的not hit rate:
| method     | A    | B    | C    | total |
| :--------- | :--- | :--- | :--- | :---- |
| kij method | 0/8  | 1/8  | 1/8  | 0.25  |
| ikj method | 0/8  | 1/8  | 1/8  | 0.25  |

## result:

### generate testing matrix:
```c
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
```

### driven code example:
```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

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

    //multiply(using different method here):
    for (int i = 0; i < A_row;i++){
        for (int j = 0; j <B_col;j++){
            int sum = 0;
            for (int k = 0; k < A_col;k++){
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }

    fclose(input);
    return 0;
}
```
### makefile setup:
```bash
CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
A_ROW = 1024
A_COL = 2048
B_ROW = 2048
B_COL = 1024

BIN = generate_matrix jik_method kij_method ijk_method kji_method jki_method ikj_method
OUT = matrix

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@


do:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./ijk_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./jik_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./jki_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./kji_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./kij_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./ikj_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)

see:
	cat matrix

clean:
	rm -rf $(OUT) *method generate_matrix
```

### testing result:
A = 1024x2048 B = 2048x1024
![](https://i.imgur.com/0GFRwoI.png)


| method       | ijk / jik     | jki & kji     | kij & ikj   |
| :----------- | :------------ | :------------ | :---------- |
| not hit rate | 1.125         | 2             | 0.25        |
| time(sec)    | 16.18 / 14.46 | 29.04 / 27.07 | 6.05 / 6.08 |



A = 2048x2048 B = 2048x2048
![](https://i.imgur.com/yzagYTa.png)


| method       | ijk / jik     | jki & kji       | kij & ikj     |
| :----------- | :------------ | :-------------- | :------------ |
| not hit rate | 1.125         | 2               | 0.25          |
| time(sec)    | 67.88 / 59.63 | 137.79 / 129.53 | 25.84 / 25.75 |

## Conclusion:
在同樣的演算法的前提下，好好的優化spatial locality對於程式的performance影響甚大!