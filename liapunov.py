import solver
import math

def energie(theta, m1, m2, g, l):
    th1 = theta[0]
    th2 = theta[1]
    dth1 = theta[2]
    dth2 = theta[3]
    V = -(m1+m2)*l*g*math.cos(th1) - m2*l*g*math.cos(th2)
    T = .5*m1*(l*dth1)**2 + .5*m2*((l*dth1)**2 + (l*dth2)**2 + 2*l*l*dth1*dth2*math.cos(th1-th2))
    return T + V
