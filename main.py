import math
import solver
import liapunov
import graphique
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #### parameters
    # mass (kg)
    m1 = 1.
    m2 = 1.
    # lenght (m)
    l=1.
    #angle (rad)
    th1 = (math.pi)
    th2 = .5*(math.pi)
    th22= .49*(math.pi)
    #
    g = 9.81
    #constants for the solver
    h = 0.01
    t_max = 15


    THETA, T = solver.pendulum(solver.p_derivatives, th1, th2, t_max, h, m1, m2, g, l)
    THETAA, T = solver.pendulum(solver.p_derivatives, th1, th22, t_max, h, m1, m2, g, l)

    #for (i,t) in enumerate(T):
    #    test = liapunov.energy(theta, m1, m2, g, l)
        #print(test)
    ani = graphique.grapher(l,THETA, THETAA, h)
    plt.show()
