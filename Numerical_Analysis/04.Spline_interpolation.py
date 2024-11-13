import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the function to compute natural cubic splines
def natural_cubic_spline(x, y):
    n = len(x) - 1
    h = [x[i+1] - x[i] for i in range(n)]
    b = [(y[i+1] - y[i]) / h[i] for i in range(n)]
    
    # Set up the system of equations
    A = np.zeros((n+1, n+1))
    B = np.zeros(n+1)
    
    # Natural spline boundary conditions
    A[0][0] = 1
    A[n][n] = 1
    
    for i in range(1, n):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
        B[i] = 3 * (b[i] - b[i-1])
    
    # Solve for the second derivatives
    c = np.linalg.solve(A, B)
    
    # Calculate coefficients for each spline segment
    splines = []
    for i in range(n):
        d = (c[i+1] - c[i]) / (3 * h[i])
        b_i = b[i] - h[i] * (2 * c[i] + c[i+1]) / 3
        splines.append((y[i], b_i, c[i], d))
    
    return splines

# Function to evaluate the spline at a given point
def evaluate_spline(splines, x, x_points):
    for i in range(len(x_points) - 1):
        if x_points[i] <= x <= x_points[i+1]:
            a, b, c, d = splines[i]
            dx = x - x_points[i]
            return a + b*dx + c*dx**2 + d*dx**3
    return None

# Function to print expanded segment functions
def print_expanded_segment_functions(splines, x_points):
    x = sp.Symbol('x')
    for i, (a, b, c, d) in enumerate(splines):
        dx = x - x_points[i]
        segment_expr = a + b * dx + c * dx**2 + d * dx**3
        expanded_expr = sp.expand(segment_expr)
        print(f"S_{i}(x) = {expanded_expr}, for x in [{x_points[i]}, {x_points[i+1]}]")

# Test data
x_points = [0, 1, 2, 3]
y_points = [0, 0.5, 2, 1.5]

# Compute the splines
splines = natural_cubic_spline(x_points, y_points)

# Print expanded segment functions
print_expanded_segment_functions(splines, x_points)

# Plotting the cubic spline interpolation
x_vals = np.linspace(min(x_points), max(x_points), 100)
y_vals = [evaluate_spline(splines, x, x_points) for x in x_vals]

plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_vals, y_vals, label='Cubic spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Natural Cubic Spline Interpolation')
plt.show()
