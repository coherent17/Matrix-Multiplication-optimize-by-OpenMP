# OpenMP

## 硬體配置:
若是使用Virtual box或是其他虛擬機器，必須要先將處理器的數量調到大於一，否則不管使用何種平行化的程式設計，結果將不會產生任何平行化的效果。(我在這邊卡了好久，原來是CPU配置的問題...)

Virtual box的處理器設定:
(原本是 1CPU調整為4CPU)
![](https://i.imgur.com/s9XN9BQ.png)

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
