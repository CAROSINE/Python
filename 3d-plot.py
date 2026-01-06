import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [10, 5, 4, 0, 1]

ax.scatter(x, y, z, c='red')
plt.show()
