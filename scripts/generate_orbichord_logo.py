import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def dim(m):
    return 3*(m-1)

def prism(m):
    n = dim(m)
    p = np.zeros((n,n))
    q = np.zeros((n,n))
    for i in range(n):
        # center
        p0 = 0.
        q0 = 0.
        # angle
        angle = 2.*np.pi*i/(3*n)
        for j in range(m-1):
            x = j/(m-1)
            y = 0
            p[i][j] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j] = x * np.sin(angle) + y * np.cos(angle)
            #p[i][j] = x
            #q[i][j] = y
            p0 += p[i][j]
            q0 += q[i][j]

        for j in range(m):
            x = 0.5*((m-j-1)/(m-1)+1)
            y = 0.866025*j/(m-1)
            p[i][j+m-1] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j+m-1] = x * np.sin(angle) + y * np.cos(angle)
            #p[i][j+m-1] = x
            #q[i][j+m-1] = y
            p0 += p[i][j+m-1]
            q0 += q[i][j+m-1]


        for j in range(m-1):
            x = 0.5*(1-j/(m-1))
            y = 0.866025*(m-j-1)/(m-1)
            p[i][j+2*m-2] = x * np.cos(angle) - y * np.sin(angle)
            q[i][j+2*m-2] = x * np.sin(angle) + y * np.cos(angle)
            #p[i][j+2*m-2] = x
            #q[i][j+2*m-2] = y
            p0 += p[i][j+2*m-2]
            q0 += q[i][j+2*m-2]

        p[i] -= p0/n
        q[i] -= q0/n

    return p, q

m = 40
n = dim(m)

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
px, py = prism(m)

c, a = 2.5, 1
x = (c + a*px) * np.cos(phi)
z = (c + a*px) * np.sin(phi)
y = a * py

fig=plt.figure()#figsize=(2,2))
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_ylim(-3,3)
ax1.plot_surface(x, y, z, rstride=3, cstride=3, cmap='coolwarm')
ax1.view_init(36, 26)
ax1.set_axis_off()
fig.savefig('orbilogo.png', transparent=True, dpi=150)
# plt.show()
