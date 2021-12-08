CC = gcc
CFLAGS = -g -Wall -std=c99 -fopenmp
CC++ = g++
C++FLAGS = -g -Wall
CHECKMEMCC = valgrind
CHECKMEMFLAGS = --leak-check=full -s --show-leak-kinds=all

#the row and column of the matrix size
matrix_length = 1024
A_ROW = $(matrix_length)
A_COL = $(matrix_length)
B_ROW = $(matrix_length)
B_COL = $(matrix_length)

EXE = generate_matrix ijk_method compare ijk_optimize
OBJ = matrix
result = golden ijk_result ijk_optimize_result

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
	echo ;\
	echo ---------Parallel by OpenMP----------- ;\
	for number in 1 2 3 4; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./ijk_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare ijk_optimize_result golden ;\
	done



# there are some error using valgrind to detect the memory error:
# It's valgrind's fault?: https://stackoverflow.com/questions/30376601/valgrind-memory-still-reachable-with-trivial-program-using-iostream
check:
	$(CHECKMEMCC) $(CHECKMEMFLAGS) ./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	$(CHECKMEMCC) $(CHECKMEMFLAGS) ./ijk_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	$(CHECKMEMCC) $(CHECKMEMFLAGS) ./compare ijk_result golden
	for number in 1 2 3 4; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		$(CHECKMEMCC) $(CHECKMEMFLAGS) ./ijk_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		$(CHECKMEMCC) $(CHECKMEMFLAGS) ./compare ijk_optimize_result golden ;\
	done

clean:
	rm -rf $(EXE) $(OBJ) $(result)