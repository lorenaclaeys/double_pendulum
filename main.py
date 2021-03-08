import math
import solver
import liapunov
import graphique

if __name__ == "__main__":
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
    for (i,t) in enumerate(T):
        test = liapunov.energie(THETA[i,:], m1, m2, g, l)
        #print(test)
