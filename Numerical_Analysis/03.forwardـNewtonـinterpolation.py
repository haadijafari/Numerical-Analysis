import numpy as np

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

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Function to calculate the value using Newton Forward Interpolation
def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    # Calculate the forward difference table
    diff_table = forward_difference_table(x_values, y_values)

    # Calculate 'h' (the difference between consecutive x_values)
    h = x_values[1] - x_values[0]
    
    # Calculate the value of 'u'
    u = (x - x_values[0]) / h
    
    # Initialize result with the first value of y_values (f(x0))
    result = y_values[0]
    
    # Newton Forward Interpolation formula
    for i in range(1, n):
        u_term = 1
        for j in range(i):
            u_term *= (u - j)
        
        result += (u_term * diff_table[0,i]) / factorial(i)
    
    return result

# Example usage:
x_values = [1, 2, 3, 4]
y_values = [2, 5, 10, 17]  # Corresponding y_values
x = 2.5  # The x value to interpolate

# Calculate the interpolated value
interpolated_value = newton_forward_interpolation(x_values, y_values, x)
print(f"The interpolated value at x = {x} is: {interpolated_value}")
