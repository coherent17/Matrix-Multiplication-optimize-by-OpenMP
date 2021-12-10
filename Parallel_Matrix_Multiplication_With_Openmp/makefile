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

OBJ = matrix
EXE = generate_matrix compare ijk_method ijk_optimize jik_method jik_optimize jki_method jki_optimize kji_method kji_optimize kij_method kij_optimize ikj_method ikj_optimize
result = golden ijk_result ijk_optimize_result jik_result jik_optimize_result jki_result jki_optimize_result kji_result kji_optimize_result kij_result kij_optimize_result ikj_result ikj_optimize_result

all: $(EXE)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

%: %.cpp
	$(CC++) $(C++FLAGS) $< -o $@

full:
	make
	make matrix
	make ijk
	make jik
	make jki
	make kji
	make kij
	make ikj

matrix:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)


ijk:
	./ijk_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare ijk_result golden
	echo ;\
	echo ----Parallel by OpenMP: ijk method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./ijk_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare ijk_optimize_result golden ;\
	done

jik:
	./jik_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare jik_result golden
	echo ;\
	echo ----Parallel by OpenMP: jik method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./jik_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare jik_optimize_result golden ;\
	done

jki:
	./jki_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare jki_result golden
	echo ;\
	echo ----Parallel by OpenMP: jki method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./jki_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare jki_optimize_result golden ;\
	done

kji:
	./kji_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare kji_result golden
	echo ;\
	echo ----Parallel by OpenMP: kji method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./kji_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare kji_optimize_result golden ;\
	done

kij:
	./kij_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare kij_result golden
	echo ;\
	echo ----Parallel by OpenMP: kij method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./kij_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare kij_optimize_result golden ;\
	done

ikj:
	./ikj_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	./compare ikj_result golden
	echo ;\
	echo ----Parallel by OpenMP: ikj method---- ;\
	for number in 2 3 4 5 6 7 8; do\
		echo -------------------------------------- ;\
		echo thread_num = $$number ;\
		./ikj_optimize $(A_ROW) $(A_COL) $(B_ROW) $(B_COL) $$number ;\
		./compare ikj_optimize_result golden ;\
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