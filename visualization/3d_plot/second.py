import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x = [5, 10, 15, 20]
z = [10, 0, 5, 15]
y = [0, 10, 5, 25]
s = [150, 130, 30, 160]
ax.scatter(x, y, z, s=s)

plt.show()