import torch

# Tensor creation
x = torch.tensor([1, 2,3])
y = torch.tensor([4, 5, 6])

print("x:", x)
print("y:", y)

# Basic operations
z = x + y
print("x + y= ", z)

#Matrix tensor shape
a = torch.rand(2, 3) # random 2X3 tensor
print(a)
print("Shape: ", a.shape)

# GPU check
print("CUDA available?", torch.cuda.is_available()) 