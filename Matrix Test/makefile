CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
A_ROW = 3
A_COL = 4
B_ROW = 4
B_COL = 3

BIN = generate_matrix 2dArray_malloc
OUT = matrix result

all: $(BIN)

generate_matrix: generate_matrix.c
	$(CC) $(CFLAGS) $< -o $@

2dArray_malloc: 2dArray_malloc.c
	$(CC) $(CFLAGS) $< -o $@

do:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./2dArray_malloc $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)

see:
	cat matrix
	cat result

clean:
	rm -rf $(OUT) $(BIN)