from numpy import sin,cos
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import solver

#### parameters
# mass (kg)
m1 = 1.
m2 = 1.
# lenght (m)
l=1.
#angle (rad)
th1 = .5*(math.pi)
th2 = 0.
#
g = 9.81
#constants for the solver
h = 0.01
t_max = 10

THETA, T = solver.pendulum(solver.p_derivatives, th1, th2, t_max, h, m1, m2, g, l)


#cartesian coordinates
x1 = l * np.sin(THETA[:,0])
y1 = -l * np.cos(THETA[:,0])
x2 = x1 + l * np.sin(THETA[:,1])
y2 = y1 - l * np.cos(THETA[:,1])

fig = plt.figure()
ax = fig.add_subplot(111,autoscale_on = False, xlim = (-2,2), ylim = (-2,2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*h))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(THETA)), interval=h*1000, blit=True, init_func=init)
plt.show()
