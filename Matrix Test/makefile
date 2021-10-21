CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
ROW = 15
COL = 15

BIN = generate_matrix test
OUT = matrix result 

all: $(BIN)

generate_matrix: generate_matrix.c
	$(CC) $(CFLAGS) $< -o $@

test: test.c
	$(CC) $(CFLAGS) $< -o $@

do:
	./generate_matrix $(ROW) $(COL)
	./test matrix result

see:
	cat matrix
	cat result

clean:
	rm -rf $(OUT) $(BIN)