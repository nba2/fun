def changerto1(anymatrix, rowsvariable, columnsvariable):
	original = anymatrix[0][0]
	while anymatrix[0][0] != 1:
		if anymatrix[0][0] == 0:
			anymatrix[0][0] = anymatrix[0][0] + 1
			anymatrix[0][columnsvariable-1] = anymatrix[0][columnsvariable-1] + 1
		else:
			for i in range(columnsvariable):
				anymatrix[0][i] = anymatrix[0][i]*(1/original)
