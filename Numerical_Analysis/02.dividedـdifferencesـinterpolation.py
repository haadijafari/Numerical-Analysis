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
def print_table_diagonal(diff_table, n):
    print("Divided Difference Table:")
    
    for i in range(2 * n):
        # Calculate the current i index
        row = int(i / 2)
        
        # Print given fi labels
        if i % 2 == 0:
            print(f'f{row} = ', end='')
        else:
            print(' ' * 5, end='')

        for j in range(0, 2 * min(row + 1, n - row), 2):
            if i % 2 == 0:
                # Print the even rows with spaces after each term
                print(f'{diff_table[row][j]:.2f}', end=' ' * 6)
            else:
                # To avoid printing elements outside the range
                if j + 1 < n - row:
                    # Print the odd rows with spaces before each term
                    print(f'{" " * 6}{diff_table[row][j + 1]:.2f}', end='')
            
            # Decrement the row value for the next iteration
            row -= 1
        
        # Move to the next line after processing a row
        print()

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

# Get input from user
while True:
    x_values = np.array([float(i) for i in input('Enter xi values (Space separated...):\n').split()], dtype=float)
    y_values = np.array([float(i) for i in input('Enter fi(xi) values (Space separated...):\n').split()], dtype=float)

    if (len(x_values) != len(y_values)):
        print('Number of xis shall be equal to number of fi(xi)s\nTry again!\n')
    else:
        break

n = len(x_values) - 1

# Generate the divided difference table
diff_table = divided_diff_table(x_values, y_values, n+1)

# Print the divided difference table with diagonal alignment
print_table_diagonal(diff_table, n + 1)

# Print Pn(x)
Pn = calc_Pn(diff_table[0], x_values)
print('*'*20)
print('P_n(x) = ', end='')
print(Pn)

# Calculate Interpolation x given by User
while True:
    x = float([float(i) for i in input('Enter Interpolation x to calculate: ').split()][0])
    if x >= min(x_values) and x <= max(x_values):
        break
    else:
        print(f'Entered x is not in range of [{min(x_values)}, {max(x_values)}]\n Try again!\n')

f_x = float(Pn.subs(symbols('x'), x))
print(f'P{n}({x:.2f}) = {f_x:.2f}')
