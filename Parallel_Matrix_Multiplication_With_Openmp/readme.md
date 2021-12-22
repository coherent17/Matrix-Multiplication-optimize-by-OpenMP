# Matrix Multiplication optimize by OpenMP
Professor: 賴伯承 Advisor: 方鈺豪 Student: 何祁恩
## Abstract:
Matrix multiplication has been widely used in scientific area, such as AI technique, semiconductor atomic calculation and so on. My project will combine all of the content I had learned in this semester. With comparing the spatial locality of the 6 types of matrix multiplication methods, apply parallel programming with OpenMP on the original process, and analyze the performance of the program.

There are three factors will affect the result:
*    The method to load/store the matrix: Spatial locality.
*    How big is the input data: Matrix size
*    Seperate the  jobs into how many part: Number of CPU 

## Process:
*    Step 1. Generate the testing input matrix with the specific matrix size, and using the ijk method to calculate the standard golden benchmark. (generate_matrix.c)
*    Step 2. For each method, read the matrix generate from Step 1 and do matrix multiplication with using different numbers of CPU. Record the multiplied part execution time, and output the multiplication result.
*    Step 3. Compare the result in Step 2 with the golden result generate in Step 1. (compare.cpp)
*    Step 4. Data visualization and analyze the execution time and the performance.

```
Note: Step1 to Step3 can be done automatically by makefile
```
Source code: https://github.com/coherent17/EE-project/tree/main/Parallel_Matrix_Multiplication_With_Openmp

## Testing Platform
NCTU ED520 Server
![](https://i.imgur.com/tfO461p.png)


## Result:

Dataset1:
Input matrix: $A_{128 \times 128} , B_{128 \times 128}$
Output matrix: $C_{128 \times 128} = A_{128 \times 128} \times B_{128 \times 128}$
Using CPU from 1~8

| method \ number of CPU |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |
|:----------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    ijk_method(msec)    | 6.23258 | 3.48444 | 2.42122 | 3.66399 | 2.97047 | 4.10529 |  6.602  | 7.08917 |
|    jik_method(msec)    | 6.20273 | 3.53585 | 2.38902 | 3.68434 | 2.99653 | 5.02316 | 6.48389 | 6.28814 |
|    jki_method(msec)    | 7.91397 | 4.8731  | 3.57016 | 5.70658 | 5.57047 | 6.50047 | 9.14202 | 8.51715 |
|    kji_method(msec)    | 8.34093 | 10.5419 | 18.4439 | 14.412  | 12.7543 | 11.029  | 14.6607 | 14.2404 |
|    kij_method(msec)    | 7.63656 | 13.1271 | 8.34934 | 7.08926 | 6.72445 | 5.71039 | 10.9151 | 12.1386 |
|    ikj_method(msec)    | 7.74122 | 4.51087 | 3.12755 | 4.74374 | 3.66672 | 4.49126 | 7.00213 |  6.904  |


Dataset2:
Input matrix: $A_{256 \times 256} , B_{256 \times 256}$
Output matrix: $C_{256 \times 256} = A_{256 \times 256} \times B_{256 \times 256}$
Using CPU from 1~8

| method \ number of CPU |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |
|:----------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    ijk_method(msec)    | 50.3707 | 28.4363 | 19.4253 | 26.2256 | 22.9331 | 19.7491 | 25.204  | 26.9415 |
|    jik_method(msec)    | 49.3684 | 27.4138 | 18.5852 | 29.227  | 23.7637 | 21.7219 | 26.0978 | 26.8812 |
|    jki_method(msec)    | 71.3667 | 41.8337 | 29.539  | 41.4873 | 39.2057 | 31.5662 | 38.1923 | 37.1664 |
|    kji_method(msec)    | 71.0206 | 80.0217 | 56.3042 | 69.4268 | 84.9929 | 61.6365 | 61.6339 | 73.0027 |
|    kij_method(msec)    | 58.3271 | 65.7669 | 57.1248 | 57.4866 | 46.6486 | 43.2105 | 54.3688 | 51.0684 |
|    ikj_method(msec)    | 57.9754 | 35.0347 | 24.3218 | 34.1153 | 28.0311 | 23.7492 | 34.1955 | 33.1445 |


Dataset3:
Input matrix: $A_{512 \times 512} , B_{512 \times 512}$
Output matrix: $C_{512 \times 512} = A_{512 \times 512} \times B_{512 \times 512}$
Using CPU from 1~8

| method \ number of CPU |    1     |    2     |    3     |    4     |    5     |    6     |    7     |    8     |
|:----------------------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|    ijk_method(sec)     | 0.469393 | 0.260219 | 0.178977 | 0.231057 | 0.208355 | 0.181413 | 0.193058 | 0.196999 |
|    jik_method(sec)     | 0.462365 | 0.258299 | 0.175686 | 0.252075 | 0.20756  | 0.177817 | 0.191762 | 0.180896 |
|    jki_method(sec)     | 0.687729 | 0.389075 | 0.264797 | 0.46951  | 0.388227 | 0.323517 | 0.362964 | 0.36719  |
|    kji_method(sec)     |  0.6849  | 0.824393 | 0.630985 | 0.55903  | 0.549017 | 0.512134 | 0.515138 | 0.475584 |
|    kij_method(sec)     | 0.470465 | 0.509372 | 0.350315 | 0.383811 | 0.367668 | 0.31437  | 0.359213 | 0.321356 |
|    ikj_method(sec)     | 0.466623 | 0.278114 | 0.190962 | 0.216237 | 0.22334  | 0.188672 | 0.229131 | 0.219322 |

Dataset4:
Input matrix: $A_{1024 \times 1024} , B_{1024 \times 1024}$
Output matrix: $C_{1024 \times 1024} = A_{1024 \times 1024} \times B_{1024 \times 1024}$
Using CPU from 1~8

| method \ number of CPU |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |
|:----------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    ijk_method(sec)     | 6.73555 | 3.59292 | 2.46217 | 3.01349 | 2.71425 | 2.40974 | 2.47131 | 2.49955 |
|    jik_method(sec)     | 6.52525 | 3.40936 | 2.32869 | 2.6249  | 2.50874 | 2.3842  | 2.53106 | 2.39937 |
|    jki_method(sec)     | 13.6443 | 7.02372 | 4.79452 | 7.03342 | 5.84557 | 5.01443 | 5.09439 | 5.07745 |
|    kji_method(sec)     |  13.78  | 13.2866 | 8.8457  | 8.51105 | 6.74901 | 5.72279 | 6.20147 | 5.78616 |
|    kij_method(sec)     | 3.72739 | 4.07834 | 2.7869  | 3.21558 | 2.76459 | 2.45544 | 2.58749 | 2.62601 |
|    ikj_method(sec)     | 3.70448 | 2.24294 | 1.54999 | 1.78363 | 1.73262 | 1.51377 | 1.59178 | 1.53354 |

Dataset5:
Input matrix: $A_{2048 \times 2048} , B_{2048 \times 2048}$
Output matrix: $C_{2048 \times 2048} = A_{2048 \times 2048} \times B_{2048 \times 2048}$
Using CPU from 1~8

| method \ number of CPU |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |
|:----------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    ijk_method(sec)     | 68.9435 | 41.5312 | 29.7924 | 29.5568 | 24.8442 |  23.83  | 23.7694 | 23.4177 |
|    jik_method(sec)     | 56.972  | 29.2092 | 20.2481 | 22.7533 | 24.8208 | 21.0675 | 21.4958 | 21.1524 |
|    jki_method(sec)     | 149.619 | 77.2311 | 56.3418 | 56.0821 | 51.2179 | 47.9171 | 48.2322 | 48.1841 |
|    kji_method(sec)     | 148.008 | 163.153 | 109.588 | 76.9565 | 62.9118 | 52.6488 | 54.4916 | 54.172  |
|    kij_method(sec)     | 29.9986 | 32.8259 | 22.3705 | 24.1346 | 21.3529 | 19.3978 | 19.6348 | 19.8231 |
|    ikj_method(sec)     | 29.6981 | 18.0958 | 16.9585 | 16.1297 | 13.886  | 11.9556 | 12.0732 | 12.0618 |

Dataset is available on my [github account](https://github.com/coherent17/EE-project/tree/main/Parallel_Matrix_Multiplication_With_Openmp/Data_visualization)

## Analysis

### Spatial locality analysis
If the spatial locality of program is good, the cache hit rate will be high, so that, it won't need so much time to load/store the data from/into the memory.

In my project, the element in matrix is int, which is 4-bytes in memory. Assume the cache line is 32-bytes, which can contained 8 integers.

In previous section, I had already finished the calculation of 6 methods: ijk, jik, jki, kji, kij, ikj. Since C is row-wise language, we can conclude that:

The cache not hit rate for 6 methods: $jki = kji > ijk = jik > kij = ikj$

The spatial locality for 6 methods: $jki = kji < ijk = jik < kij = ikj$

However, when paralleling the program into several CPUs to calculate, there exist the data-dependency problem. Two threads want to change the same element at the same time. In $kji,kij$ method, I need to deal with the data-dependency problem, which will stop all threads, and wait for the previous thread to finish its job then continue.


Different methods of matrix multiplication v.s. Execution time and the performance ratio to only using 1 CPU.
![](https://i.imgur.com/yDBSYsE.png)
In matrix size = 2048, we can see the result clearly.
*    $t_{jki},t_{kji}>t_{ijk},t_{jik}>t_{kij},t_{ikj}$, because of the spatial locality(cache not hit rate)
*    $t_{kji}>t_{jki}$, although thier cache not hit rate is the same, but in method kji I need to deal with the data-dependency problem, therefore the time is longer
*    $t_{kij}>t_{ikj}$, although thier cache not hit rate is the same, but in method kji I need to deal with the data-dependency problem, therefore the time is longer
*    The performance of the programming related to only use 1 CPU(no parallel) is shown on the right side. 

![](https://i.imgur.com/F7Lbuit.png)
![](https://i.imgur.com/4I0qZQL.png)
*    In matrix size = 512, the data-dependency caused effect is more apparent than matrix size =1024, 2048, therefore, the execution time is longer.
![](https://i.imgur.com/KBYAPUF.png)
![](https://i.imgur.com/Q3DWmAE.png)
*    In matrix size = 256, 128. There exist a performance peak at using 3 CPUs.


### Matrix size analysis
Everyone can guess that as the matrix size grow, it need more time to finish the matrix multiplication for CPU. For how much does the matrix length affect the execution time, and for how much will the performance improve when applied the parallel programming? I will show you in this block.

![](https://i.imgur.com/jV4Ul1N.png)
*    When using 1 CPU, there is no data-dependency problem, $t_{kji}\approx t_{jki}$, $t_{ijk}\approx t_{jik}$, $t_{kij}\approx t_{ikj}$ as we had explained before.
![](https://i.imgur.com/tvRJbMf.png)
![](https://i.imgur.com/VjSGxox.png)
![](https://i.imgur.com/CQElYNr.png)
*    When using more than 1 CPU, the data-dependency problem exist. And therefore, the time for kji and kij method need to stall and wait for other threads to finish their job. The execution time will increase.