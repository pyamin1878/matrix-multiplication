import torch

## Define two matrices as PyTorch tensors

matrix_1 = torch.tensor([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

matrix_2 = torch.tensor([[0,1,2],
                        [3,4,5],
                        [6,7,8]])

# Calculate the dot product of matrix_1 and matrix_2 using .matmul()

product = torch.matmul(matrix_1, matrix_2)

# Print resulting matrix

print(product)