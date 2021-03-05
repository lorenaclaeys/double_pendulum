def Energie(th1,th2):
    g=9.81
    dth1 = 0 #derivatives(t, theta)[0]
    dth2 = 0 #derivatives(t, theta)[1]
    V = -m1*g*l*math.cos(th1)-m2*g*l*(math.cos(th1)+math.cos(th2))
    T = .5*m1*(l*dth1)**2+ .5*m2*l**(2)*(dth1**2 + dth2**2 + 2*dth1*dth2(math.sin(th1)*math.sin(th2) + math.cos(th1)*math.cos(th2)))
    return T + V


print(Energie(th1, th2))
