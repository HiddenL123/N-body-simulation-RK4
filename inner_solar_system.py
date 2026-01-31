import numpy as np
from body import Body
inner_solar_system = []

# --------------------
# SUN
# --------------------
inner_solar_system.append(Body(
    1.9885e30,
    np.array([0.0, 0.0, 0.0]),
    np.array([0.0, 0.0, 0.0])
))

# --------------------
# MERCURY
# --------------------
inner_solar_system.append(Body(
    3.3011e23,
    np.array([5.7909e10, 0.0, 0.0]),
    np.array([0.0, 4.79e4, 0.0])
))

# --------------------
# VENUS
# --------------------
inner_solar_system.append(Body(
    4.8675e24,
    np.array([1.0821e11, 0.0, 0.0]),
    np.array([0.0, 3.50e4, 0.0])
))

# --------------------
# EARTH
# --------------------
earth_pos = np.array([1.495978707e11, 0.0, 0.0])
earth_vel = np.array([0.0, 2.9785e4, 0.0])

inner_solar_system.append(Body(
    5.9722e24,
    earth_pos,
    earth_vel
))

# Moon
inner_solar_system.append(Body(
    7.342e22,
    earth_pos + np.array([3.844e8, 0.0, 0.0]),
    earth_vel + np.array([0.0, 1.022e3, 0.0])
))

# --------------------
# MARS
# --------------------
mars_pos = np.array([2.279e11, 0.0, 0.0])
mars_vel = np.array([0.0, 2.41e4, 0.0])

inner_solar_system.append(Body(
    6.4171e23,
    mars_pos,
    mars_vel
))

# Phobos
inner_solar_system.append(Body(
    1.0659e16,
    mars_pos + np.array([9.378e6, 0.0, 0.0]),
    mars_vel + np.array([0.0, 2.138e3, 0.0])
))

# Deimos
inner_solar_system.append(Body(
    1.4762e15,
    mars_pos + np.array([2.343e7, 0.0, 0.0]),
    mars_vel + np.array([0.0, 1.351e3, 0.0])
))