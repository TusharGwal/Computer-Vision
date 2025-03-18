# CS512 Computer Vision - Assignment 0

## Overview
This assignment covers foundational concepts in linear algebra and neural networks, focusing on their application in computer vision. It includes **4 parts**:
1. **Vector operations**
2. **Matrix operations**
3. **Eigenvalues/Eigenvectors**
4. **Neural network basics**

The code demonstrates computations using Python libraries like `NumPy` and `SymPy`, with implementations of key mathematical operations and activation functions.

---

## Assignment Parts

### Part A: Vector Operations
- **Topics**: Vector arithmetic, projections, cross/dot products, direction cosines, linear independence.
- **Key Results**:
  - Computed `3p + 2q = [6, 3, 22]`.
  - Verified non-linear independence of vectors `p, q, r` using determinants.
  - Derived vector perpendicular to both `p` and `q` using cross product.

### Part B: Matrix Operations
- **Topics**: Matrix addition/multiplication, determinants, inverses, projections, solving linear systems.
- **Key Results**:
  - Calculated determinants for matrices `X` and `Z`.
  - Solved linear systems (e.g., `Yt = s`).
  - Demonstrated outer products (`pqt`) and scalar projections.

### Part C: Eigenvalues and Eigenvectors
- **Topics**: Eigendecomposition, orthogonality, solving homogeneous equations.
- **Key Results**:
  - Eigenvalues of `M = [3.5±1.32j]` with complex eigenvectors.
  - Showed eigenvectors of symmetric matrix `N` are orthogonal.
  - Solved `Pt = 0` for trivial/non-trivial solutions using `SymPy`.

### Part D: Neural Network Basics
- **Topics**: Activation functions (sigmoid, ReLU), layer-wise computation.
- **Key Results**:
  - Pre-activation output: `z = 1.15`.
  - Post-activation outputs using **sigmoid** (`0.759`) and **ReLU** (`1.15`).
  - Multi-layer computation with ReLU and sigmoid activations.

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `NumPy` for vector/matrix operations.
  - `SymPy` for symbolic matrix computations.
  - `math` for basic mathematical functions.

---

## Setup & Usage
1. **Install Dependencies**:
   ```bash
   pip install numpy sympy
