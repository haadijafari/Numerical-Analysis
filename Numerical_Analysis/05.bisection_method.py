def bisection_method(func, a, b, epsilon):
    # Check the initial condition
    if func(a) * func(b) >= 0:
        raise ValueError("The function does not change sign in the given interval. Please choose a different interval.")
    
    while (b - a) > epsilon:
        midpoint = (a + b) / 2
        f_mid = func(midpoint)
        
        if f_mid == 0:  # If the exact root is found
            return midpoint
        elif func(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2  # Approximate root

# Input from the user
if __name__ == "__main__":
    import math  # Import math for functions like sin, exp, etc.
    
    # Dynamically define the function
    print("Note: Use math.sin(x), math.exp(x), etc., for functions.")
    func_str = input("Enter the function in terms of x (e.g., math.sin(x) - 0.5): ")
    func = lambda x: eval(func_str)
    
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    epsilon = float(input("Enter the value of epsilon: "))
    
    try:
        root = bisection_method(func, a, b, epsilon)
        print(f"The approximate root of the function in the interval [{a}, {b}] is: {root}")
    except ValueError as e:
        print(f"Error: {e}")
