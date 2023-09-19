import numpy as np

# Input two matrices as NumPy arrays
matrix_1 = np.array([[1,2,3],  
                    [4,5,6],
                    [7,8,9]])

matrix_2 = np.array([[0,1,2],
                    [3,4,5],
                    [6,7,8]])

# Calculate the dot product of matrix_1 and matrix_2 using NumPy's dot function
res = np.dot(matrix_1,matrix_2)

# Print resulting matrix
print(res)