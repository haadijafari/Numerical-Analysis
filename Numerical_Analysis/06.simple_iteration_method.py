def simple_iteration_method(g, x0, epsilon, max_iterations=1000):
    """
    Simple Iteration Method to find the root of an equation.

    Parameters:
    g (function): The iterative function g(x).
    x0 (float): Initial guess.
    epsilon (float): Tolerance for convergence.
    max_iterations (int): Maximum number of iterations.

    Returns:
    float: Approximate root.
    """
    x = x0
    for i in range(max_iterations):
        next_x = f(x)
        if abs(next_x - x) < epsilon:
            print(f"Converged in {i + 1} iterations.")
            return next_x
        x = next_x
    
    raise ValueError("Did not converge within the maximum number of iterations.")

# Input from the user
if __name__ == "__main__":
    import math

    # Dynamically define the function g(x)
    print("Note: Rewrite the equation as x = f(x). Use math.sin(x), math.exp(x), etc., for functions.")
    f_str = input("Enter the function f(x) for iteration (e.g., (math.exp(-x)): ")
    f = lambda x: eval(f_str)
    
    x0 = float(input("Enter the initial guess x0: "))
    epsilon = float(input("Enter the value of epsilon: "))
    
    try:
        root = simple_iteration_method(f, x0, epsilon)
        print(f"The approximate root is: {root}")
    except ValueError as e:
        print(f"Error: {e}")
