import numpy as np

# Create matrices using np.arange and np.reshape which are two 3x3 matrices
matrix_1 = np.arange(1,10).reshape(3,3)

matrix_2 = np.arange(0,9).reshape(3,3)

# Calculate the dot product of matrix_1 and matrix_2 using NumPy's dot function
res = np.dot(matrix_1,matrix_2)

# Print resulting matrix
print(res)