import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9]
y1 = [10,20,40,55,58,55,50,40,20,10]

plt.fill_between(x,y1,0,
                 facecolor='orange',
                 color='blue',
                 alpha=0.2)

plt.show()