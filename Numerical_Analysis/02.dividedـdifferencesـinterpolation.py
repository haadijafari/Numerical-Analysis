import numpy as np
from sympy import expand, symbols


# Function to calculate divided difference table
def divided_diff_table(x, y, n):
    # Create a table with zeros
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y  # First column is the y values
    
    # Fill the divided differences in the table
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (x[i + j] - x[i])
    
    return diff_table

# Function to print the divided difference table in diagonal format
def print_table_diagonal(diff_table, n, x):
    print("Divided Difference Table:")
    for i in range(n):
        # Print the first column (y values)
        print(f"f({x[i]}) = {diff_table[i][0]:.2f}")
        
        # For other columns, add indentation to create the diagonal effect
        for j in range(1, n - i):
            print(((" " * (j * 20)) if j==1 else (" " * (j * 15))) + f"{diff_table[i][j]:.2f}")

# Function to calculate the Pn(x) and simplify it using expand function
def calc_Pn(coef: list, x: list):
    n = len(coef)
    Pn = ''
    
    # Constant term f[x0]
    Pn += f"{coef[0]:.2f}"
    
    # For each remaining term, build the polynomial
    for i in range(1, n):
        Pn += f"{coef[i]:+.2f}"  # Sign and coefficient for the term
        
        # Now add the factors (x - x_j) for j = 0 to i-1
        for j in range(i):
            Pn += f"*(x-{x[j]:.2f})"
    return expand(Pn)

# Sample data points
x_values = np.array([5, 6, 9, 11, 13, 16], dtype=float)
y_values = np.array([12, 13, 14, 16, 20, 22], dtype=float)

n = len(x_values) - 1

# Generate the divided difference table
diff_table = divided_diff_table(x_values, y_values, n+1)

# Print the divided difference table with diagonal alignment
print_table_diagonal(diff_table, n+1, x_values)


Pn = calc_Pn(diff_table[0], x_values)
print('*'*20)
print('P_n(x) = ', end='')
print(Pn)

while True:
    x = float([float(i) for i in input('Enter Interpolation x to calculate: ').split()][0])
    if x >= min(x_values) and x <= max(x_values):
        break
    else:
        print(f'Entered x is not in range of [{min(x_values)}, {max(x_values)}]\n Try again!\n')

f_x = float(Pn.subs(symbols('x'), x))
print(f'P{n}({x:.2f}) = {f_x:.2f}')
