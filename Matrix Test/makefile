CC = gcc
CFLAGS = -g -Wall

#the row and column of the matrix size
A_ROW = 1024
A_COL = 2048
B_ROW = 2048
B_COL = 1024

BIN = generate_matrix jik_method kij_method ijk_method kji_method jki_method ikj_method
OUT = matrix

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@


do:
	./generate_matrix $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./ijk_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./jik_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./jki_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./kji_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./kij_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)
	time ./ikj_method $(A_ROW) $(A_COL) $(B_ROW) $(B_COL)

see:
	cat matrix

clean:
	rm -rf $(OUT) *method generate_matrix