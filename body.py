import numpy as np
class Body:
    def __init__(self, mass, x, v = np.zeros(3).copy()):
        self.m = mass
        self.x = x  # current position
        self.xtemp = x  # temp position

        self.v = v  # current velocity
        self.vtemp = v  # temp velocity

        self.a = np.zeros(3)  # current acceleration
        self.atemp = np.zeros(3)  # temp acceleration


        self.kx1 = None
        self.kx2 = None
        self.kx3 = None
        self.kx4 = None

        self.kv1 = None
        self.kv2 = None
        self.kv3 = None
        self.kv4 = None
        

        self.trajectory = []
    
    def record(self):
        self.trajectory.append(self.x.copy())