from numpy import sin,cos
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import solver

def grapher(l, THETA, THETAA, h):
    #cartesian coordinates
    x1 = l * np.sin(THETA[:,0])
    y1 = -l * np.cos(THETA[:,0])
    x2 = x1 + l * np.sin(THETA[:,1])
    y2 = y1 - l * np.cos(THETA[:,1])

    x1A = l * np.sin(THETAA[:,0])
    y1A = -l * np.cos(THETAA[:,0])
    x2A = x1A + l * np.sin(THETAA[:,1])
    y2A = y1A - l * np.cos(THETAA[:,1])

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
        thisx = [x2[i], x1[i], 0, x1A[i], x2A[i]]
        thisy = [y2[i], y1[i], 0, y1A[i], y2A[i]]


        line.set_data(thisx, thisy)

        time_text.set_text(time_template % (i*h))
        return line, time_text

    ani = animation.FuncAnimation(fig, animate, range(1, len(THETA)), interval=h*1000, blit=True, init_func=init)
    return ani
