# OpenMP

## 硬體配置:
若是使用Virtual box或是其他虛擬機器，必須要先將處理器的數量調到大於一，否則不管使用何種平行化的程式設計，結果將不會產生任何平行化的效果。(我在這邊卡了好久，原來是CPU配置的問題...)

Virtual box的處理器設定:
(原本是 1CPU調整為4CPU)
![](https://i.imgur.com/s9XN9BQ.png)
調整完後，在terminal輸入:
```bash=
$ lscpu
```
便可以看到CPU的即時情況，也可以看到有4CPU(S)的資訊
![](https://i.imgur.com/HRy7WrK.png)


## Start OpenMP
在使用OpenMP前要先引入標頭檔:
```c=
#include <omp.h>
```
先來看個簡單的範例:
```c=
//multithread_test.c
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
```
其中"#pragma omp parallel"是告訴程式在後面的括號中要進行多執行續的模式。
```bash=
#makefile:
CC = gcc
CFLAGS = -g -Wall -fopenmp
OBJ = multithread_test

all: $(OBJ)

%: %.c
	$(CC) $(CFLAGS) $< -o $@
do:
	./multithread_test

clean:
	rm $(OBJ)
```
而後在linux的編譯環境下，若是要使用OpenMP的function，則需要在編譯時加上編譯參數"-fopenmp"，才能成功的致能。編譯後執行的結果如下:
![](https://i.imgur.com/5X0P5Tu.png)
可以觀察到在多執行緒的區塊中printf被執行了四次(預設執行緒為4:defaut # of thread = 4)。

## 設定執行緒數量:
```c=
//用來設定要有多少個執行緒
#pragma omp parallel num_threads()

//也可以先設定要有多少執行緒，再做平行化:
omp_set_thread_num()
#pragma omp parallel
    
//得知是第幾個執行緒(index從0開始):
int omp_get_thread_num()
```

```c=
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
```
結果:
![](https://i.imgur.com/3pe8quV.png)

可以看到若是初始化執行緒數量為n，則thread num =0~n-1

## 平行化for loop:
有兩種方法，如下:都是先設定執行緒的數量為4，而後針對for loop進行平行化。
```c=
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
```
結果:
![](https://i.imgur.com/S5nXxLJ.png)

可以看到這兩種方法都確實將for loop要做的工作分配給了4個CPU個別去執行。另外，也可以從印出的結果發現OpenMP在分配工作給CPU時，是將連續的區塊分給同一個CPU，剛好也滿足先前所提到的spatial locality的優化。接下來便要將openmp的平行化程式設計應用在先前提到的矩陣乘法上。