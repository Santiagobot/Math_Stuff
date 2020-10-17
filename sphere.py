import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 100


theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

x = np.cos(phi)*np.sin(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(theta)


fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_zlim(-1,1)
ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax1.view_init(46, 26)
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_zlim(-1,1)
ax2.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax2.view_init(0, 0)
ax2.set_xticks([])
plt.show()
