import numpy as np
from body import Body
G = 6.6743e-11


def verlet_simulate(bodies, dt=3600, steps=24*365, softening=1e6):
    # Initial half-kick
    for b in bodies:
        print("initial", b.x)
        b.v += 0.5 * b.a * dt
    
    for _ in range(steps):
        # DRIFT
        for b in bodies:
            b.record()
            b.x += b.v * dt
            b.a[:] = 0.0

        # COMPUTE a
        for i in range(len(bodies) - 1):
            for j in range(i + 1, len(bodies)):
                b0 = bodies[i]
                b1 = bodies[j]
                r = b1.x - b0.x
                dist = np.linalg.norm(r) + softening
                a0 = G * b1.m * r / dist**3
                a1 = -G * b0.m * r / dist**3
                b0.a += a0
                b1.a += a1
        
        # KICK (full step for middle iterations)
        for b in bodies:
            b.v += b.a * dt
    
    # Final half-kick to synchronize
    for b in bodies:
        b.v -= 0.5 * b.a * dt
        print("final", b.x)


def get_acc(r, b1m, dist3):
    return G * b1m* r / dist3

def runge_kutta(bodies, dt=3600*3, steps=365*8, softening=1e6):
    h = dt
    for _ in range(steps):
        # get kv1
        for i in range(len(bodies) - 1):
            for j in range(i+1, len(bodies)):
                b0 = bodies[i]
                b1 = bodies[j]

                r = b1.x - b0.x
                dist3 = (np.linalg.norm(r) + softening)**3
                b0.a += get_acc(r, b1.m, dist3)
                b1.a += get_acc(-r, b0.m, dist3)

        for i in range(len(bodies)):
            b = bodies[i]
            b.kv1 = b.a[:]
            b.kx1 = b.v[:]

            x = b.x[:]
            v = b.v[:]

            b.xtemp = x + b.kx1 * h/2
            b.vtemp = v + b.kv1 * h/2

            b.a = np.zeros(3)

        # get kv2
        for i in range(len(bodies) - 1):
            for j in range(i+1, len(bodies)):
                b0 = bodies[i]
                b1 = bodies[j]

                r = b1.xtemp - b0.xtemp
                dist3 = (np.linalg.norm(r) + softening)**3
                b0.a += get_acc(r, b1.m, dist3)
                b1.a += get_acc(-r, b0.m, dist3)
        
        for i in range(len(bodies)):
            b = bodies[i]
            b.kv2 = b.a[:]
            b.kx2 = b.vtemp[:]

            x0 = b.x[:]
            v0 = b.v[:]

            b.xtemp = x0 + b.kx2 * h/2
            b.vtemp = v0 + b.kv2 * h/2

            b.a = np.zeros(3)
        
        # get kv3
        for i in range(len(bodies) - 1):
            for j in range(i+1, len(bodies)):
                b0 = bodies[i]
                b1 = bodies[j]

                r = b1.xtemp - b0.xtemp
                dist3 = (np.linalg.norm(r) + softening)**3
                b0.a += get_acc(r, b1.m, dist3)
                b1.a += get_acc(-r, b0.m, dist3)
        
        for i in range(len(bodies)):
            b = bodies[i]
            b.kv3 = b.a[:]
            b.kx3 = b.vtemp[:]

            x0 = b.x[:]
            v0 = b.v[:]

            b.xtemp = x0 + b.kx3 * h
            b.vtemp = v0 + b.kv3 * h

            b.a = np.zeros(3)
        
        # get kv4
        for i in range(len(bodies) - 1):
            for j in range(i+1, len(bodies)):
                b0 = bodies[i]
                b1 = bodies[j]

                r = b1.xtemp - b0.xtemp
                dist3 = (np.linalg.norm(r) + softening)**3
                b0.a += get_acc(r, b1.m, dist3)
                b1.a += get_acc(-r, b0.m, dist3)
        
        for i in range(len(bodies)):
            b = bodies[i]
            b.kv4 = b.a[:]
            b.kx4 = b.vtemp

            b.x += (h/6)*(b.kx1 + 2*b.kx2 + 2*b.kx3 + b.kx4)
            b.v += (h/6)*(b.kv1 + 2*b.kv2 + 2*b.kv3 + b.kv4)

            b.record()
            b.a = np.zeros(3)
        

G = 6.67430e-11

DAY = 24 * 3600         # seconds

solar_system = []
solar_system.append(Body(1.9885e30, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0])))
solar_system.append(Body(5.9722e24, np.array([1.495978707e11, 0.0, 0.0]), np.array([0.0, 2.9785e4, 0.0])))
solar_system.append(Body(7.342e22,  np.array([1.49982271e11, 0.0, 0.0]), np.array([0.0, 3.0807e4, 0.0])))


from solar_system import solar_system
from inner_solar_system import inner_solar_system

if __name__ == "__main__":
    bodies = []
    for _ in range(5):
        x = 1e12 * np.random.random(3).astype(float)
        mass = 1e24 * np.random.random()
        bodies.append(Body(mass, x))

    system = inner_solar_system
    runge_kutta(system, dt = 10*60, steps = 6*24*365)
    #hermite_simulate(solar_system)
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))

    for b in system:
        traj = np.array(b.trajectory)
        plt.plot(traj[:, 0], traj[:, 1])

    plt.axis("equal")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectories")
    plt.show()
    



