import tensorflow as tf  # type: ignore

# Tensor creation
x = tf.constant([1, 2, 3])
y = tf.constant([3, 4, 5])

print("X: ", x)
print("Y: ", y)

#Basic operation
z = x + y
print("Z: ",z)

#Random Tensor
a = tf.random.uniform((2, 3))
print(a)
print("Shape of a: ", a.shape)

#GPU check
print("GPU available: ", tf.config.list_physical_devices('GPU'))