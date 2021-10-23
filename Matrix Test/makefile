CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
A_ROW = 3
A_COL = 4
B_ROW = 4
B_COL = 3

BIN = generate_matrix 1dArray 2dArray linkedlist
OUT = matrix result

all: $(BIN)

generate_matrix: generate_matrix.c
	$(CC) $(CFLAGS) $< -o $@

1dArray: 1dArray.c
	$(CC) $(CFLAGS) $< -o $@

2dArray: 2dArray.c
	$(CC) $(CFLAGS) $< -o $@

linkedlist: linkedlist.c
	$(CC) $(CFLAGS) $< -o $@

do:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	rm generate_matrix
	./1dArray $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./2dArray $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)

see:
	cat matrix

clean:
	rm -rf $(OUT) $(BIN)