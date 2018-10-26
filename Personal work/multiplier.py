from matrix import * ##imports relevant functions
print("First, enter your first matrix (A) into the program.")
matrixA = matrixmaker() ##defines first matrix
print("Now, enter the second matrix (B) into the program.")
matrixB = matrixmaker() ##defines second matrix
assert len(matrixA[0]) == len(matrixB) ##confirms that matrices can be multiplied together
matrixAB = [None]*len(matrixA) ##creates all necessary rows in product, matrixAB
for i in range(len(matrixA)):
    matrixAB[i] = [None]*len(matrixB[0]) ##creates all necessary columns in product, matrixAB

print(matrixA)
print(matrixB)
##MAB[0][0], MAB[1][0], MAB[2][0]
