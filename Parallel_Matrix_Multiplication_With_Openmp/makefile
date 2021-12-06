CC = gcc
CFLAGS = -g -Wall -std=c99
CC++ = g++
C++FLAGS = -g -Wall

#the row and column of the matrix size
matrix_length = 1024
A_ROW = $(matrix_length)
A_COL = $(matrix_length)
B_ROW = $(matrix_length)
B_COL = $(matrix_length)

EXE = generate_matrix ijk_method compare
OBJ = matrix
result = golden ijk_result

all: $(EXE)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

%: %.cpp
	$(CC++) $(C++FLAGS) $< -o $@

matrix:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)


ijk:
	./ijk_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare ijk_result golden

clean:
	rm -rf $(EXE) $(OBJ) $(result)