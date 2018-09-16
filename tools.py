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
