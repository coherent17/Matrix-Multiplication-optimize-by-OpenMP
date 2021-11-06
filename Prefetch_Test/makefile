version = release

CC = gcc

ifeq ($(version), ENABLE)
all: by_rows_with_prefetch by_cols_with_prefetch
CFLAGS = -g -Wall -DENABLE_prefetch -O3
else
all: by_rows by_cols
CFLAGS = -g -Wall -O3
endif

by_rows_with_prefetch: prefetch_by_rows.c
	$(CC) $(CFLAGS) $< -o $@

by_cols_with_prefetch: prefetch_by_cols.c
	$(CC) $(CFLAGS) $< -o $@

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
	rm by_rows_with_prefetch by_rows by_cols_with_prefetch by_cols