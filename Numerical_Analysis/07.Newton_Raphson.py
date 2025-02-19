import math
import sympy as sp

def newton_raphson(f, df, x0, epsilon):
    """
    Finds the root of the equation f(x) = 0 using the Newton-Raphson method.

    Parameters:
    f (function): The function for which the root is to be found.
    df (function): The derivative of the function f.
    x0 (float): Initial guess for the root.
    epsilon (float): Tolerance for the root approximation.

    Returns:
    tuple: The root of the function and the value of f(root).
    """
    x = x0
    while True:
        fx = f(x)
        dfx = df(x)
        if abs(fx) < epsilon:
            return x, fx
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        x = x - fx / dfx

# Example usage:
if __name__ == "__main__":
    # Get the function f(x) from the user
    f_str = input("Enter the function f(x) (e.g., x**3 - x - 2): ")
    
    # Compute the derivative automatically
    x = sp.Symbol('x')
    f_sympy = sp.sympify(f_str)
    df_sympy = sp.diff(f_sympy, x)
    
    # Convert to Python functions
    f = sp.lambdify(x, f_sympy, "math")
    df = sp.lambdify(x, df_sympy, "math")
    
    print(f"Computed derivative f'(x): {df_sympy}")
    
    # Get initial guess and tolerance
    x0 = float(input("Enter the initial guess x0: "))
    epsilon = float(input("Enter the value of epsilon: "))
    
    try:
        root, f_root = newton_raphson(f, df, x0, epsilon)
        print(f"The root is: {root}")
        print(f"The value of f at the root (f(root)) is: {f_root}")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
