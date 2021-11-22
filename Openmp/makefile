CC = gcc
CFLAGS = -g -Wall -fopenmp
OBJ = multithread_test thread_number

all: $(OBJ)

%: %.c
	$(CC) $(CFLAGS) $< -o $@
do:
	./thread_number

clean:
	rm $(OBJ)