import numpy as np
from tqdm import tqdm
import time

G = 6.6743e-11
MINUTE = 60
HOUR = 3600
DAY = 24 * HOUR
YEAR = 365.24 * DAY

def create_t(x, softening=1e6):
    """
    Computes the interaction tensor T where T[i, p, j] represents the 
    p-th Cartesian component of the gravitational influence of body j on body i.
    
    Formula: T[i][p][j] = (x_j[p] - x_i[p]) / ||x_j - x_i||^3
    
    Args:
        x (ndarray): (N, 3) array of positions for N bodies.
        softening (float): Small constant to prevent division by zero.
        
    Returns:
        ndarray: (N, 3, N) interaction tensor.
    """
    # x shape: (N, 3)
    # R shape: (N, N, 3) -> R[i, j] is the vector from i to j
    R = x[np.newaxis, :, :] - x[:, np.newaxis, :]
    
    dist_sq = np.sum(R**2, axis=-1) + softening**2
    kernel = dist_sq**(-1.5) # shape: (N, N)
    
    # Current T: (N, N, 3)
    T = kernel[:, :, np.newaxis] * R
    
    # Transpose to (N, 3, N)
    return np.transpose(T, (0, 2, 1))

def f(y, Gm, softening, N):
    """
    Computes the state derivative (dy/dt) for the N-body system.
    
    Maps the current state y = [v; x] to its derivative 
    f(y) = [a; v]
    
    Formula:
        f(y) = [ d/dt(v) ] = [ a(x) ]
               [ d/dt(x) ]   [  v   ]
    
    Args:
        y (ndarray): (2N, 3) state tensor where y[:N] is velocity and y[N:] is position.
        Gm (ndarray): (N,) vector of gravitational parameters (G * mass) for each body.
        softening (float): Softening length for gravitational interactions.
        N (int): Number of bodies in the system.

    Returns:
        ndarray: (2N, 3) derivative tensor containing [acceleration; velocity].
    """
    v_curr = y[:N]
    x_curr = y[N:]
            
    # Compute acceleration: a = T(x) @ Gm using dot product
    T = create_t(x_curr, softening)
    a = T @ Gm
            
    # Return [a; v] stacked vertically
    return np.vstack((a, v_curr))


def runge_kutta(bodies, dt=3600*3, steps=365*8, softening=1e6):
    """
    Integrates the N-body system using the 4th-order Runge-Kutta method.
    
    Args:
        bodies (list): A list of Body objects containing initial mass, position, and velocity.
        dt (float): Time step in seconds
        steps (int): Number of steps to perform.
        softening (float): Softening parameter passed to the derivative function f().

    Formula:
        y_next = y_curr + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
        
        Split into components:
        v_next = v_curr + (dt/6) * (kv1 + 2*kv2 + 2*kv3 + kv4)
        x_next = x_curr + (dt/6) * (kx1 + 2*kx2 + 2*kx3 + kx4)

        k1:
            kv1 = a(x)
            kx1 = v
        k2:
            kv2 = a(x + dt/2 * kx1)
            kx2 = v + dt/2 * kv1
        k3:
            kv3 = a(x + dt/2 * kx2)
            kx2 = v + dt/2 * kv2
        k4:
            kv4 = a(x + dt * kx3)
            kx4 = v + dt * kv3

    Returns:
        ndarray: A (steps, N, 3) array containing the position history of all bodies.
    """
    h = dt
    hd2 = h/2
    hd6 = h/6
    Gm = G * np.array([b.m for b in bodies])
    N = len(bodies)
    
    traj_data = np.empty((steps, N, 3))
    # y = (v,x)
    y = np.empty((2 * N, 3))
    y[:N] = [b.v for b in bodies]
    y[N:] = [b.x for b in bodies]

    for i in tqdm(range(steps), desc="Simulating"):

        k1 = f(y, Gm, softening, N)
        k2 = f(y + hd2 * k1, Gm, softening, N)
        k3 = f(y + hd2 * k2, Gm, softening, N)
        k4 = f(y + h * k3, Gm, softening, N)

        y += hd6 * (k1 + 2*k2 + 2*k3 + k4)
    
        traj_data[i] = y[N:]
    return traj_data

from n_body_systems.solar_system import solar_system
from n_body_systems.inner_solar_system import inner_solar_system
from n_body_systems.earth_moon_sun import earth_moon_sun

class Config():
    """
    A configuration container for N-body simulation parameters.

    Attributes:
        system (list): List of Body objects to be simulated.
        dt (float): The time step size in seconds (delta t).
        steps (int): Total number of steps.
        softening (float): A softening constant to avoid numerical 
            divergence to infinity during close encounters (default 1e6).
        N (int): The number of bodies in the system
    """
    def __init__(self, system, dt, steps, softening=1e6):
        self.system = system
        self.dt = dt
        self.steps = steps
        self.softening = softening
        self.N = len(system)

    def __iter__(self):
        yield self.system
        yield self.dt
        yield self.steps
        yield self.softening
    
    
if __name__ == "__main__":
    cur_conf = Config(inner_solar_system, dt=10*MINUTE, steps=6*24*365) # inner solar system, 10 minute steps, 1 years
    #cur_conf = Config(inner_solar_system, dt=10*MINUTE, steps=10*6*24*365) # inner solar system, 10 minute steps, 10 years
    #cur_conf = Config(earth_sun_moon, dt=1*MINUTE, steps=6*24*28) # earth sun moon, 1 minute steps, 1 month
    #cur_conf = Config(earth_sun_moon, dt=10*MINUTE, steps=6*24*365) # earth sun moon, 10 minute steps, 1 year
    #cur_conf = Config(earth_sun_moon, dt=10*MINUTE, steps=10*6*24*365) # earth sun moon, 10 minute steps, 10 years
    #cur_conf = Config(solar_system, dt=10*MINUTE, steps=6*24*365) # full solar system, 10 minute steps, 1 year
    #cur_conf = Config(solar_system, dt=10*MINUTE, steps=10*6*24*365) # full solar system, 10 minute steps, 10 years
    #cur_conf = Config(solar_system, dt=60*MINUTE, steps=100*6*24*365) # full solar system, 1 hour steps, 100 years note: phobos and deimos are unstable with large step
    
    current = time.time()
    # traj shape: (steps, N, 3)
    traj_data = runge_kutta(*cur_conf) 

    print(f"Simulation Elapsed: {time.time() - current:.2f} seconds")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 8))

    # Iterate through each body by index
    for i in range(cur_conf.N):
        # Extract all time steps for body 'i', dimensions x (0) and y (1)
        x_coords = traj_data[:, i, 0]
        y_coords = traj_data[:, i, 1]
        
        plt.plot(x_coords, y_coords, label=f"Body {i}")

    plt.axis("equal")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlabel("x (meters)")
    plt.ylabel("y (meters)")
    plt.title("Vectorized N-Body Trajectories")
    # plt.legend() # Optional: add labels if you have names for the bodies
    plt.show()
    



