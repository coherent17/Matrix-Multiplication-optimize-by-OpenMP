CC = gcc
CFLAGS = -g -Wall -O2
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