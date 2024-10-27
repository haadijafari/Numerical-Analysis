import numpy as np
from sympy import expand, symbols

# Function to calculate the forward difference table
def forward_difference_table(x_values, y_values):
    n = len(x_values)
    # Creating the forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y_values  # First column is y_values

    # Filling the table
    for i in range(1, n):
        for j in range(n - i):
            diff_table[j,i] = diff_table[j+1,i-1] - diff_table[j,i-1]

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

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Function to calculate the Pn(x) and simplify it using expand function
# def calc_Pn(coef: list, x: list):
#     n = len(coef)
#     Pn = ''
    
#     # Constant term f[x0]
#     Pn += f"{coef[0]:.2f}"
    
#     # For each remaining term, build the polynomial
#     for i in range(1, n):
#         Pn += f"{coef[i]:+.2f}"  # Sign and coefficient for the term
        
#         # Now add the factors (x - x_j) for j = 0 to i-1
#         for j in range(i):
#             Pn += f"*(x-{x[j]:.2f})"
#     return expand(Pn)

# Function to calculate the value using Newton Forward Interpolation
def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    # Calculate the forward difference table
    diff_table = forward_difference_table(x_values, y_values)

    # Calculate 'h' (the difference between consecutive x_values)
    h = x_values[1] - x_values[0]
    
    # Calculate the value of 'u'
    s = (x - x_values[0]) / h
    
    # Initialize result with the first value of y_values (f(x0))
    result = y_values[0]
    
    # Newton Forward Interpolation formula
    for i in range(1, n):
        u_term = 1
        for j in range(i):
            u_term *= (s - j)
        
        result += (u_term * diff_table[0,i]) / factorial(i)
    
    return result

# Example usage:
x_values = [1, 2, 3, 4]
y_values = [2, 5, 10, 17]  # Corresponding y_values
x = 2.5  # The x value to interpolate

# Calculate the interpolated value
interpolated_value = newton_forward_interpolation(x_values, y_values, x)
print(f"The interpolated value at x = {x} is: {interpolated_value}")

diff_table = forward_difference_table(x_values, y_values)
print_table_diagonal(diff_table, n = len(x_values))
