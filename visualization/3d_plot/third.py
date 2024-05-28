import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_wireframe(x, y, z)

plt.show()