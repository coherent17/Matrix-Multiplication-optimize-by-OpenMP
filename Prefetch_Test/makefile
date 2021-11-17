CC = gcc
CFLAGS = -g -Wall -O2
OBJS = by_rows by_cols by_rows_with_prefetch by_cols_with_prefetch

all: $(OBJS)

by_rows_with_prefetch: prefetch_by_rows.c
	$(CC) $(CFLAGS) -DENABLE_prefetch $< -o $@

by_cols_with_prefetch: prefetch_by_cols.c
	$(CC) $(CFLAGS) -DENABLE_prefetch $< -o $@

by_rows:prefetch_by_rows.c
	$(CC) $(CFLAGS) $< -o $@

by_cols:prefetch_by_cols.c
	$(CC) $(CFLAGS) $< -o $@

time:
	time ./by_rows_with_prefetch
	time ./by_rows
	time ./by_cols_with_prefetch
	time ./by_cols

clean:
	rm $(OBJS)