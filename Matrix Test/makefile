CC = gcc
CFLAGS = -g -Wall

BIN = generate_matrix test
OUT = matrix result 

all: $(BIN)

generate_matrix: generate_matrix.c
	$(CC) $(CFLAGS) $< -o $@

test: test.c
	$(CC) $(CFLAGS) $< -o $@

do:
	./generate_matrix
	./test matrix result

see:
	cat matrix
	cat result

clean:
	rm -rf $(OUT) $(BIN)