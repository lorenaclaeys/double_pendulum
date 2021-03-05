import numpy as np
import math
#### parameters
# mass (kg)
m1 = 1.
m2 = 2.
# lenght (m)
l=1
#angle (rad)
th1 = .5*(math.pi)
th2 = 0

#constants for the solver
h = 0.01
t_max = 10


def rk_4(derivatives, theta, t, h):
    k_1 = derivatives(t,theta)
    k_2 = derivatives(t + .5*h, theta + .5*h*k_1)
    k_3 = derivatives(t + .5*h, theta + .5*h*k_2)
    k_4 = derivatives(t + h, theta + h*k_3)
    return (k_1 + 2*k_2 + 2*k_3 + k_4)/6.

def pendulum(derivatives, th1, th2, t_max, h):
    N = int(1 + t_max/h)
    THETA = np.zeros((N,4))
    # condition initiale:
    THETA[0, 0] = th1
    THETA[0, 1] = th2
    T = np.linspace(0, t_max, N)
    for (i,t) in enumerate(T[1:]):
        theta = THETA[i, :]
        THETA[i+1, :] = theta + h*rk_4(derivatives, theta, t, h)
    return THETA, T

def derivatives(t, theta):
    g = 9.81
    th1 = theta[0]
    th2 = theta[1]
    dth1 = theta[2]
    dth2 = theta[3]
    denom = 1/(m1 + m2*math.sin(th1 - th2)**2)
    a = m2*(g/l)*math.sin(th2)*math.cos(th1 -th2)
    b = (dth1**2)*math.cos(th1-th2) + (dth2**2)
    c = (m1 + m2)*(g/l)*math.sin(th1)

    d = m2*(dth2**2)*math.sin(th1 - th2)*math.cos(th1 -th2)
    e = (g/l)*math.sin(th1)*math.cos(th1 -th2)
    f = (dth1**2)*math.sin(th1 - th2)
    g = (g/l)*math.sin(th2)
    return np.array([dth1, dth2, (denom)*(a - m2*math.sin(th1 - th2)*(b - c)), (denom)*(d + (m1 + m2)*(e + f - g))])


test = pendulum(derivatives, th1, th2, t_max, h)
print(test)
