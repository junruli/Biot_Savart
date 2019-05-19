import numpy as np
import matplotlib.pyplot as plt
#position vector in x, y ,z
class coil(object):
    def __init__(self, R = 0 , I = 0, position = 0):
        self.R = R
        self.I = I
        self.z = position

    def field(self, field_point = np.array([0,0,0])):
    #finite element
        N = 100
        dthe = 2*3.1415926/N
        field_strength = 0
        for n in range(1,N):
            the = n*dthe
            dl = np.array([-self.R * np.sin(the),self.R*np.cos(the),0])*dthe
            rl = np.array([self.R*np.cos(the), self.R*np.sin(the),self.z])
            r_p = field_point-rl
            field_strength= self.I * np.cross(dl,r_p)/np.power(np.linalg.norm(r_p),3) + field_strength
        return field_strength

A = coil(1,1,0.5)
B = coil(1,-1,-0.5)
r = []
field = []
for j in range(0,15):
    R = np.array([j/5,0,0])
    r.append(j/4)
    tdfield = A.field(R)+B.field(R)
    field.append(tdfield[0])
plt.scatter(r, field)
plt.show()
#test
