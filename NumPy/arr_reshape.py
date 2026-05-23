import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print("1D: ",a)
print("Shape: ", a.shape) # shape means size

print("")
b= a.reshape(2,3) # reshape a to 2 rows and 3 columns
print("2D:", b)
print("Shape: ", b.shape)


print("")
c = a.reshape(2, 3, 1) # reshape a to 2 rows, 3 columns and 1 depth
print("3D: ", c)
print("Shape: ", c.shape)
