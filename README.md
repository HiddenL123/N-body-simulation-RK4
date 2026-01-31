# N-body-simulation-RK4
A high-performance Python implementation of an N-body gravitational simulator with 4th-order Runge-Kutta integration and a vectorized tensor-based approach to compute gravitational interactions

Key Features

  Vectorized Physics: Uses NumPy broadcasting to compute all N2 interactions in a single operation, avoiding slow Python for loops.

  RK4 Stability: Implements the classic 4th-order Runge-Kutta method, providing significantly better energy conservation and orbital stability than Euler or Midpoint methods.

  Phase-Space Integration: Consolidates system state into a (2N,3) tensor y=[v;x], allowing the entire solar system to be updated as a single mathematical entity.

  Softening Factor: Includes Plummer softening to handle close encounters and prevent numerical singularities.
    

Mathematical Approach
    
  1. State-Space

  $$y = \begin{bmatrix} v \\\\ x \end{bmatrix}$$
  
  $$\frac{dy}{dt} = f(y) = \begin{bmatrix} a(x) \\\\ v \end{bmatrix}$$
  
  2. Interaction Tensor
  
  $$T_{i,p,j} = \frac{x_{j,p} - x_{i,p}}{(|x_j - x_i|^2 + \epsilon^2)^{1.5}}$$
  
  $$a = T \cdot (Gm)$$
  
  3. RK4 Stages
  
  $$k_1 = f(y_n)$$
  
  $$k_2 = f(y_n + \frac{\Delta t}{2} k_1)$$
  
  $$k_3 = f(y_n + \frac{\Delta t}{2} k_2)$$
  
  $$k_4 = f(y_n + \Delta t k_3)$$
  
  $$y_{n+1} = y_n + \frac{\Delta t}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$

a=T⋅Gm

Usage:
