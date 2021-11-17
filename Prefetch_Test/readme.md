# Prefetch data in cache

## Why prefetch?
在電腦存取一個蠻大的2D Array時，不管是在讀取row或是col都會發生cache not hit。因此我們可以使用prefetch的功能預先讀取之後想要存取的記憶體位址，以降低cache not hit的機率。

## 實作:
這次要改善的程式很簡單，有一個2D Array，分別沿著row及col加總內部所有元素的值。並且使用__builtin_prefetch這個函數來預先讀取可能會發生cache miss的地方。看看會得到甚麼改善。
```c=
//by_rows.c
for (i = 0; i < ROWS;i++){
    for (j = 0; j < COLS;j++){
        sum+= matrix[i][j];
    }
}
```
```c=
//by_cols.c
for (j = 0; j < COLS;j++){
    for (i = 0; i < ROWS;i++){
        sum+= matrix[i][j];
    }
}
```
由上面這兩個簡單的程式可以看出:
*    by_rows.c:
        *    若cache line = 32 bytes = 8 * sizeof(int)，若是row的size大於8的話，則勢必會發生cache miss。而行之間，也會因為記憶體不連續而發生not hit，因此每當換到下一個row時，必定會發生not hit的情況。

*    by_cols.c
        *    若是沿著col來讀，可以發現每一次的加總都會發生cache not hit，為一個space locality很差的程式。

### Prefetch function:

```c=
__builtin_prefetch (const void *addr, rw, locality)
```
*    第一個argument填入的是想要prefetch的指標
*    第二個argument填入的是0或是1(0:read, 1:write)
*    第三個argument填入的是locality分為0~3分，取決於日後是否還會access這個位址

### 改善Not hit by __builtin_prefetch:
```c=
//prefetch_by_rows.c
for (i = 0; i < ROWS;i++){
    for (j = 0; j < COLS;j++){
        sum+= matrix[i][j];
        if(j+1<COLS && ((j+1)-1)%8==0){
            __builtin_prefetch(&matrix[i][j+1], 0, 3);
        }
    }
    if(i+1<ROWS){
        __builtin_prefetch(&matrix[i+1][j], 0, 3);
    }
}
```

```c=
//prefetch_by_cols.c
for (j = 0; j < COLS;j++){
    for (i = 0; i < ROWS;i++){
        sum+= matrix[i][j];
        if(i+1<ROWS){
            __builtin_prefetch(&matrix[i+1][j], 0, 0);
        }
    }
    if(j+1<COLS){
        __builtin_prefetch(&matrix[i][j+1], 0, 0);
    }
}
```
**這兩個程式(prefetch_by_rows.c與preetch_by_cols.c)在先前所提到可能會發生cache miss的地方使用了prefetch去增加cache hit rate。**
```bash=
# makefile setup
CC = gcc
CFLAGS = -g -Wall
OBJS = by_rows by_cols prefetch_by_rows prefetch_by_cols

all: $(OBJS)

%: %.c
	$(CC) $(CFLAGS)  $< -o $@

time:
	time ./by_rows
	time ./prefetch_by_rows
	time ./by_cols
	time ./prefetch_by_cols

clean:
	rm $(OBJS)
```
## 結果:

| case | compiler optimize | by_rows.c | prefetch_by_rows.c | by_cols.c | prefetch_by_cols.c |
|:----:|:-----------------:|:---------:|:------------------:|:---------:|:------------------:|
|  1   |        -O2        |   8.71    |        9.30        |   26.38   |       23.43        |
|  2   |        -O3        |   8.52    |        9.19        |   25.02   |       23.56        |


### Case1
![](https://i.imgur.com/eSE3tOk.png)


### Case2
![](https://i.imgur.com/HUA2vL5.png)

## 結論:
在by_row的比較中，因為程式本身就是space locality比較好的程式，再根據可能會cache miss的地方進行prefetch可能會使整個程式的instruction count增加許多，而使得效能的改善比較不明顯。而在by_col的比較中，則是可以明顯看到效能有提升一些些。雖然能夠透過prefetch來預存資料，但是寫出好的space locality才是比較根本的方法。