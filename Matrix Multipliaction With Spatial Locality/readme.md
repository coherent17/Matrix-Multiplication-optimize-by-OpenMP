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
![](https://i.imgur.com/l11YUpD.png)
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

### **jki method & kji method**
![](https://i.imgur.com/llerSs0.png)
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

### **kij method & ikj method**
![](https://i.imgur.com/lr3NMXL.png)
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