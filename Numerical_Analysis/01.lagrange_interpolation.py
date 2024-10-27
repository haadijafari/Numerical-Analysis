from sympy import expand

def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange interpolation to compute the polynomial Pn(x)
    
    Parameters:
    x_values: List of x points
    y_values: List of corresponding y values (y = f(x))
    x: The point at which we want to evaluate Pn(x)
    
    Returns:
    The value of the polynomial at x
    """
    n = len(x_values)
    Pn_x = 0
    poly_term = [[] for i in range(n)]
    
    # Calculate Lagrange polynomial
    for i in range(n):
        L_i = 1
        poly_term[i] = ['', 1]
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
                poly_term[i][0] += (('(x-' if poly_term[i][0] == '' else '*(x-') + (str(x_values[j]) if x_values[j] >= 0 else f'({x_values[j]})') + ')')
                poly_term[i][1] *= (x_values[i] - x_values[j])

        
        Pn_x += y_values[i] * L_i
    
    return Pn_x, poly_term

# Example usage

while True:
    x_values = [float(i) for i in input('Enter xi values (Space separated...):\n').split()]
    y_values = [float(i) for i in input('Enter fi(xi) values (Space separated...):\n').split()]

    if (len(x_values) != len(y_values)):
        print('Number of xis shall be equal to number of fi(xi)s\nTry again!\n')
    else:
        break

while True:
    x = float([float(i) for i in input('Enter Interpolation x to calculate: ').split()][0])
    if x >= min(x_values) and x <= max(x_values):
        break
    else:
        print(f'Entered x is not in range of [{min(x_values)}, {max(x_values)}]\n Try again!\n')

print('*'*20)
result = lagrange_interpolation(x_values, y_values, x)
print(f"P{len(x_values)}({x}) = {result[0]}\n")
print(f'P{len(x_values)}(x) = ', end='')
pn = ''
for i, L_i in enumerate(result[1]):
    term_i = f'{L_i[0]}/({str(L_i[1])})*({str(y_values[i])})'
    pn += ('+' + term_i) if pn != '' else term_i
print(expand(pn))
