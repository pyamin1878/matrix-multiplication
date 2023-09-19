# Input two matrices and label them

matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix_2 = [[0,1,2],
            [3,4,5],
            [6,7,8]]

# Create an empty result matrix to store the multiplication result
res = [[0 for x in range (3)] for y in range(3)]

# Use nested for loops to iterate through rows and columns of the matrices
for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_2)):

            # Calculate the element at row 'i' and column 'j' of the result matrix
            res[i][j] += matrix_1[i][k] * matrix_2[k][j]

# Print the resulting matrix
print(res)
