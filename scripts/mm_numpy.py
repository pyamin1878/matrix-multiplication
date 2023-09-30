# Import numpy for matrix operations

import numpy as np

def get_user_matrix(dimensions_prompt, elements_prompt):
    """
    Get a matrix from the user based on provided prompts for dimensions and elements.
    """
    rows, cols = map(int, input(dimensions_prompt).split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    return np.array(matrix)

def generate_random_matrix(rows, cols, min_val=0, max_val=10):
    """
    Generate a random matrix with given dimensions and element value range.
    """
    return np.random.randint(min_val, max_val+1, (rows, cols))

# Main Function

def matrix_multiply_numpy(matrix_1, matrix_2):
    """
    Multiply two matrices using numpy's dot function.
    """
    if matrix_1.shape[1] != matrix_2.shape[0]:
        return "Matrices cannot be multiplied due to incompatible dimensions."
    return np.dot(matrix_1, matrix_2)

def matrix_multiply_extended(option="manual", matrix_1=None, matrix_2=None):
    """
    Multiply two matrices either manually entered, randomly generated, or provided.
    """
    if option == "manual":
        matrix_1 = get_user_matrix("Enter dimensions for Matrix 1: ", "Enter elements for Matrix 1: ")
        matrix_2 = get_user_matrix("Enter dimensions for Matrix 2: ", "Enter elements for Matrix 2: ")
    elif option == "random":
        rows_1, cols_1 = 3, 3  # Modify as needed
        rows_2, cols_2 = 3, 3  # Modify as needed
        matrix_1 = generate_random_matrix(rows_1, cols_1)
        matrix_2 = generate_random_matrix(rows_2, cols_2)
    return matrix_multiply_numpy(matrix_1, matrix_2)

# Example usage (commented out; can be uncommented for testing)
# result = matrix_multiply_extended(option="random")
# print("Result of matrix multiplication:", result)