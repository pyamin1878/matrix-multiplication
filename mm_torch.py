import torch

matrix_1 = torch.tensor([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

matrix_2 = torch.tensor([[0,1,2],
                        [3,4,5],
                        [6,7,8]])

product = torch.matmul(matrix_1, matrix_2)

print(product)