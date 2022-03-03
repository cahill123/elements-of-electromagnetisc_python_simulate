import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return np.sqrt((10-x**2-y**2)/2)

limit = 2.23606
x = np.linspace(-limit, limit, 30)
y = np.linspace(-limit, limit, 30)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D contour')
plt.show()