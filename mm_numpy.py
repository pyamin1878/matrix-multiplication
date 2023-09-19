import numpy as np

#Input two matrices
matrix_1 = np.array([[1,2,3],  
                    [4,5,6],
                    [7,8,9]])

matrix_2 = np.array([[0,1,2],
                    [3,4,5],
                    [6,7,8]])

# Return dot product
res = np.dot(matrix_1,matrix_2)

# print resulting matrix
print(res)