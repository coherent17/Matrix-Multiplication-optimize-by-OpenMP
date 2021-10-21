CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
A_ROW = 2
A_COL = 3
B_ROW = 3
B_COL = 2

BIN = generate_matrix tranditional
OUT = matrix result 

all: $(BIN)

generate_matrix: generate_matrix.c
	$(CC) $(CFLAGS) $< -o $@

tranditional: tranditional.c
	$(CC) $(CFLAGS) $< -o $@

do:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./tranditional $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)

see:
	cat matrix
	cat result

clean:
	rm -rf $(OUT) $(BIN)