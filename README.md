##Runge Kutta vectorized N body simulation

---

# N-Body Simulation (RK4)

A Python implementation of an **N-body gravitational simulator** using **4th-order Runge–Kutta (RK4)** time integration and a fully **vectorized tensor-based** acceleration computation.

---

## Key Features

### Vectorized Physics

* Uses **NumPy broadcasting** to compute all gravitational interactions in a single tensor operation.

### RK4 Time Integration

* Implements the classic **4th-order Runge–Kutta (RK4)** method for N body simulations.

### Velocity, Position representation

* The entire system is represented as a single phase-space matrix:
  
  $$
  y =
  \begin{bmatrix}
  v \\\\
  x
  \end{bmatrix}
  \in \mathbb{R}^{3\times (2N)}
  $$
* This allows for fast parallelized computation with numpy.

### Softening for Close Encounters

* Includes **Plummer softening** to prevent numerical singularities during close approaches:

  $$\epsilon > 0$$

---

## Requirements

* **Python 3.13**
* Dependencies:

```bash
pip install numpy matplotlib tqdm
```

---

## Quick Start

1. **Configure the simulation**  
   Comment/uncomment sections of the code or modify configuration variables
   (e.g. time step, softening length, creating a new system or use a different preset).

2. **Run the simulation**
   ```bash
   python main.py
---


## Mathematical Formulation

### 1. State-Space Dynamics

$$
y =
\begin{bmatrix}
v \\\\
x
\end{bmatrix},
\quad
\frac{dy}{dt} = f(y) =
\begin{bmatrix}
a(x) \\\\
v
\end{bmatrix}
$$

---

### 2. Interaction Tensor

For positions 

$$ x \in \mathbb{R}^{3 \times N} )$$ 

the interaction tensor is defined as:

$$
T_{i,p,j}= \frac{x_{j,p} - x_{i,p}}{\left(\lVert x_j - x_i \rVert^2 + \epsilon^2 \right)^{3/2}}
$$

The acceleration of each body is computed via:

$$
a = T \cdot (Gm)
$$

where:

* $G$ is the gravitational constant  
* $m \in \mathbb{R}^N$ is the mass vector

---

### 3. Runge–Kutta 4 (RK4) Integration


$$\begin{aligned}
k_1 &= f(y_n) \\
k_2 &= f\left(y_n + \frac{\Delta t}{2} k_1\right) \\
k_3 &= f\left(y_n + \frac{\Delta t}{2} k_2\right) \\
k_4 &= f\left(y_n + \Delta t, k_3\right)
\end{aligned}$$



$$y_{n+1} = y_n +
\frac{\Delta t}{6}
\left(
k_1 + 2k_2 + 2k_3 + k_4
\right)
]$$

---


* Write a **benchmark or energy-conservation section**
* Adapt this for a **GitHub research-style README** with figures and results
