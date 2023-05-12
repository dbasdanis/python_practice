import numpy as np
import matplotlib
import matplotlib.pyplot as plt


N_numbers = 100000
N_bins = 100

np.random.seed(0)

x,y = np.random.multivariate_normal(
    mean=[0.0,0.0],
    cov=[[1.0,0.4],
         [0.4,0.25]],
         size=N_numbers
    ).T

plt.hist2d(x,y,bins=N_bins,cmap='plasma')

# Plot a colorbar with label
cb = plt.colorbar()
cb.set_label('Number of entries')

plt.title('Heatmap of 2D normally distributed data points')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()