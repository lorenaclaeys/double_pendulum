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

    delta = th2 - th1
    denom = (m1 + m2) * l - m2*l*math.cos(delta)*math.cos(delta)
    ddth1 = ((m2*l*(dth1**2)*math.sin(delta)*math.cos(delta) + m2*g*math.sin(th2)*math.cos(delta) + m2*l*(dth2**2)*math.sin(delta) - (m1 + m2)*g*math.sin(th1))/ denom)
    ddth2 = ((- m2*l*(dth2**2)*math.sin(delta)*math.cos(delta) + (m1 + m2)*g*math.sin(th1)*math.cos(delta) - (m1 + m2)*l*(dth1**2)*math.sin(delta) - (m1 + m2)*g*math.sin(th2))/ denom)

    return np.array([dth1, dth2, ddth1, ddth2])
