from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N_numbers = 100000
N_bins = 20

np.random.seed(0)

x, y = np.random.multivariate_normal(
    mean=[0.0, 0.0], # mean
    cov=[[1.0, 0.4],
        [0.4, 0.25]], # covariance matrix
    size=N_numbers
    ).T # transpose to get columns

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(x, y, bins=N_bins)

plt.title('3D histogram of 2D normally distributed data points')
plt.xlabel('x axis')
plt.ylabel('y axis')

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.show()
