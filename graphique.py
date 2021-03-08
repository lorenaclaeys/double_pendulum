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
th2 = 0
#
g = 9.81
#constants for the solver
h = 0.01
t_max = 10


THETA, T = solver.pendulum(solver.p_derivatives, th1, th2, t_max, h, m1, m2, g, l)

#cartesian coordinates
x1 = l * np.sin(THETA[:,0])
y1 = l * np.cos(THETA[:,0])
x2 = x1 + l * np.sin(THETA[:,1])
y2 = y1 - l * np.cos(THETA[:,1])
print(x1,x2,y1,y2)
