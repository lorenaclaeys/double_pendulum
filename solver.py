import numpy as np
import math

def rk_4(derivatives, theta, t, h, m1, m2, g, l):
    k_1 = derivatives(t, theta, m1, m2, g, l)
    k_2 = derivatives(t + .5*h, theta + .5*h*k_1, m1, m2, g, l)
    k_3 = derivatives(t + .5*h, theta + .5*h*k_2, m1, m2, g, l)
    k_4 = derivatives(t + h, theta + h*k_3, m1, m2, g, l)
    return (k_1 + 2*k_2 + 2*k_3 + k_4)/6.

def pendulum(derivatives, th1, th2, t_max, h, m1, m2, g, l):
    N = int(1 + t_max/h)
    THETA = np.zeros((N,4))
    # condition initiale:
    THETA[0, 0] = th1
    THETA[0, 1] = th2
    T = np.linspace(0, t_max, N)
    for (i,t) in enumerate(T[1:]):
        theta = THETA[i, :]
        THETA[i+1, :] = theta + h*rk_4(derivatives, theta, t, h, m1, m2, g, l)
    return THETA, T

def p_derivatives(t,theta, m1, m2, g, l):
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
    j = (g/l)*math.sin(th2)
    return np.array([dth1, dth2, (denom)*(a - m2*math.sin(th1 - th2)*(b - c)), (denom)*(d + (m1 + m2)*(e + f - j))])

#only to test rk_4
def free_fall(derivatives, x0, t_max, h, g):
    N = int(1 + t_max/h)
    X = np.zeros((N,2))
    # condition initiale:
    X[0, 0] = x0
    T = np.linspace(0, t_max, N)
    for (i,t) in enumerate(T[1:]):
        x = X[i, :]
        X[i+1, :] = x + h*rk_4(derivatives, x, t, h, 0., 0., g, 0.)
    return X, T

def ff_derivatives(t, xx, m1, m2, g, l):
    x = xx[0]
    dx = xx[1]
    return np.array([dx, g])

#X, ts = free_fall(ff_derivatives, 10., 1., .01, -9.81)
