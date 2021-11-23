CC = gcc
CFLAGS = -g -Wall -fopenmp
OBJ = multithread_test thread_number parallel_for_loop_test

all: $(OBJ)

%: %.c
	$(CC) $(CFLAGS) $< -o $@
do:
	./parallel_for_loop_test

clean:
	rm $(OBJ)