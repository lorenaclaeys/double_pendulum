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

if __name__ == "__main__":
    #### parameters
    # mass (kg)
    m1 = 1.
    m2 = 1.
    # lenght (m)
    l=1
    #angle (rad)
    th1 = .5*(math.pi)
    th2 = 0
    #
    g = 9.81
    #constants for the solver
    h = 0.01
    t_max = 10


    THETA, T = solver.pendulum(solver.p_derivatives, th1, th2, t_max, h, m1, m2, g, l)
    for (i,t) in enumerate(T):
        test = energie(THETA[i,:], m1, m2, g, l)
        print(test)
