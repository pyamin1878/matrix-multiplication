import torch

#input two matrices

matrix_1 = torch.tensor([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

matrix_2 = torch.tensor([[0,1,2],
                        [3,4,5],
                        [6,7,8]])

# dot product with .matmul()

product = torch.matmul(matrix_1, matrix_2)

# print resulting matrix

print(product)