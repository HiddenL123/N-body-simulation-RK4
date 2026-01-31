import numpy as np
from body import Body
solar_system = []

# --------------------
# SUN
# --------------------
solar_system.append(Body(
    1.9885e30,
    np.array([0.0, 0.0, 0.0]),
    np.array([0.0, 0.0, 0.0])
))

# --------------------
# MERCURY
# --------------------
solar_system.append(Body(
    3.3011e23,
    np.array([5.7909e10, 0.0, 0.0]),
    np.array([0.0, 4.79e4, 0.0])
))

# --------------------
# VENUS
# --------------------
solar_system.append(Body(
    4.8675e24,
    np.array([1.0821e11, 0.0, 0.0]),
    np.array([0.0, 3.50e4, 0.0])
))

# --------------------
# EARTH
# --------------------
earth_pos = np.array([1.495978707e11, 0.0, 0.0])
earth_vel = np.array([0.0, 2.9785e4, 0.0])

solar_system.append(Body(
    5.9722e24,
    earth_pos,
    earth_vel
))

# Moon
solar_system.append(Body(
    7.342e22,
    earth_pos + np.array([3.844e8, 0.0, 0.0]),
    earth_vel + np.array([0.0, 1.022e3, 0.0])
))

# --------------------
# MARS
# --------------------
mars_pos = np.array([2.279e11, 0.0, 0.0])
mars_vel = np.array([0.0, 2.41e4, 0.0])

solar_system.append(Body(
    6.4171e23,
    mars_pos,
    mars_vel
))

# Phobos
solar_system.append(Body(
    1.0659e16,
    mars_pos + np.array([9.378e6, 0.0, 0.0]),
    mars_vel + np.array([0.0, 2.138e3, 0.0])
))

# Deimos
solar_system.append(Body(
    1.4762e15,
    mars_pos + np.array([2.343e7, 0.0, 0.0]),
    mars_vel + np.array([0.0, 1.351e3, 0.0])
))

# --------------------
# JUPITER
# --------------------
jup_pos = np.array([7.785e11, 0.0, 0.0])
jup_vel = np.array([0.0, 1.307e4, 0.0])

solar_system.append(Body(
    1.8982e27,
    jup_pos,
    jup_vel
))

# Galilean moons
solar_system.append(Body(8.93e22,  jup_pos + np.array([4.217e8, 0, 0]), jup_vel + np.array([0, 1.734e4, 0])))  # Io
solar_system.append(Body(4.80e22,  jup_pos + np.array([6.711e8, 0, 0]), jup_vel + np.array([0, 1.371e4, 0])))  # Europa
solar_system.append(Body(1.48e23,  jup_pos + np.array([1.070e9, 0, 0]), jup_vel + np.array([0, 1.088e4, 0])))  # Ganymede
solar_system.append(Body(1.08e23,  jup_pos + np.array([1.883e9, 0, 0]), jup_vel + np.array([0, 8.204e3, 0])))  # Callisto

# --------------------
# SATURN
# --------------------
sat_pos = np.array([1.433e12, 0.0, 0.0])
sat_vel = np.array([0.0, 9.68e3, 0.0])

solar_system.append(Body(
    5.6834e26,
    sat_pos,
    sat_vel
))

# Titan
solar_system.append(Body(
    1.3452e23,
    sat_pos + np.array([1.222e9, 0, 0]),
    sat_vel + np.array([0, 5.57e3, 0])
))

# --------------------
# URANUS
# --------------------
ura_pos = np.array([2.872e12, 0.0, 0.0])
ura_vel = np.array([0.0, 6.80e3, 0.0])

solar_system.append(Body(
    8.6810e25,
    ura_pos,
    ura_vel
))

# Titania
solar_system.append(Body(
    3.527e21,
    ura_pos + np.array([4.364e8, 0, 0]),
    ura_vel + np.array([0, 3.64e3, 0])
))

# --------------------
# NEPTUNE
# --------------------
nep_pos = np.array([4.495e12, 0.0, 0.0])
nep_vel = np.array([0.0, 5.43e3, 0.0])

solar_system.append(Body(
    1.02413e26,
    nep_pos,
    nep_vel
))

# Triton
solar_system.append(Body(
    2.14e22,
    nep_pos + np.array([3.547e8, 0, 0]),
    nep_vel + np.array([0, 4.39e3, 0])
))