def matrix_multiply_nested_loops(matrix_1, matrix_2):
    # Get dimensions of the input matrices
    rows_1, cols_1 = len(matrix_1), len(matrix_1[0])
    rows_2, cols_2 = len(matrix_2), len(matrix_2[0])

    # Check if the matrices can be multiplied
    if cols_1 != rows_2:
        return "Matrix dimensions do not match"

    # Create an empty result matrix
    res = [[0 for x in range(cols_2)] for y in range(rows_1)]

    # Use nested for loops to iterate through rows and columns of the matrices
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(rows_2):
                # Calculate the element at row 'i' and column 'j'
                res[i][j] += matrix_1[i][k] * matrix_2[k][j]
    
    return res

# Test the function
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

res = matrix_multiply_nested_loops(matrix_1, matrix_2)
print("Resulting matrix:", res)

