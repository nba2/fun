rows = int(input("How many rows are in your matrix? "))
columns = int(input("How many columns are in your matrix? ")) ##first two lines define size of matrix to variables r and c.
matrix = [None]*rows ##establishes list called "matrix" with r entries of None.
for i in range(rows):
	matrix[i] = [None]*columns ##For each entry between 0 and r in "matrix," replaces entry with list of c entries of None.
for i in range(rows):
	for j in range(columns):
		if j == 0:
			print("You are in row {:d}.".format(i + 1))
		matrix[i][j] = float(input("Enter the value for the element in column {:d}: ".format(j + 1)))
from tools import *
changerto1(matrix, rows, columns)
print(matrix)
