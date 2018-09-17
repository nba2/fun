def matrixmaker():
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
	return matrix
def changerto1(anymatrix, rowsvariable, columnsvariable):
	original = anymatrix[0][0]
	while anymatrix[0][0] != 1:
		if anymatrix[0][0] == 0:
			firstrow = anymatrix[0]
			for i in range(rowsvariable-1):
				anymatrix[i] = anymatrix[i + 1]
				anymatrix[rowsvariable-1] = firstrow
		else:
			for i in range(columnsvariable):
				anymatrix[0][i] = anymatrix[0][i]*(1/original)
