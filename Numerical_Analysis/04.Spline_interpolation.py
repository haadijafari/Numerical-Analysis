import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def cubic_spline(x, y):
    n = len(x) - 1
    A_matrix = np.zeros(shape=((n - 1), (n - 1)))
    for i in range(len(A_matrix)):
        if i - 1 >= 0:
            A_matrix[i][i - 1] = x[i+1] - x[i] #hi
        A_matrix[i][i] = 2 * ((x[i+1] - x[i]) + (x[i+2] - x[i+1]))
        if i + 1 < len(A_matrix):
            A_matrix[i][i + 1] = x[i+2] - x[i+1]

    f_xi = []
    for i in range(len(y) - 1):
        f_xi.append((y[i+1] - y[i]) / (x[i+1] - x[i]))
    f_xi = np.array(f_xi)

    B_matrix = [f_xi[i+1] - f_xi[i] for i in range(len(f_xi) - 1)]

    m_i = np.linalg.solve(A_matrix, B_matrix)
    m_i = np.insert(m_i, 0, 0) #m0
    m_i = np.insert(m_i, len(m_i), 0) #last m
    
    d_i = []
    c_i = []
    for i in range(n):
        di = y[i] - (x[i+1] - x[i]) ** 2 * m_i[i]
        d_i.append(di)

        ci = f_xi[i] + (x[i+1] - x[i])*(m_i[i] - m_i[i+1])
        c_i.append(ci)


    s_i = ['' for _ in range(n)]

    for i in range(n):
        exp_1 = f'(((x-{x[i+1]})**3)/{(x[i+1] - x[i])})*{m_i[i]}'
        exp_2 = f'((((x-{x[i]})**3)*{m_i[i+1]})/{(x[i+1] - x[i])})'
        exp_3 = f'{c_i[i]}*(x-{x[i]})'
        exp_4 = f'{d_i[i]}'
        s_i[i] = sp.expand(f'-{exp_1} + {exp_2} + {exp_3} + {exp_4}')

    return s_i


def print_cubic_spline(spline_list, x):
    for i in range(len(spline_list)):
        print(f'S{i}(x) = {spline_list[i]}\tif\t{x[i]} <= x <= {x[i+1]}')


def calculate_interpolation(spline_list, x_values, x):
    for i in range(len(x_values  - 1)):
        if x_values[i] <= x <= x_values[i+1]:
            return sp.expand(str(spline_list[i]).replace('x', '(' + str(x) + ')'))


def draw_graph(spline, x_values):
    x_fine = np.linspace(min(x_values), max(x_values), 1000)  # Fine x values for smooth curve
    y_fine = []
    
    for x in x_fine:
        y_fine.append(sp.N(calculate_interpolation(spline, x_values, x)))

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'o', label='Given Points')  # Plot original points
    plt.plot(x_fine, y_fine, label='Cubic Spline')          # Plot spline
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    


# Get inputs
while True:
    x_values = np.array([float(i) for i in input('Enter xi values (Space separated...):\n').split()], dtype=float)
    y_values = np.array([float(i) for i in input('Enter fi(xi) values (Space separated...):\n').split()], dtype=float)

    if (len(x_values) != len(y_values)):
        print('Number of xis shall be equal to number of fi(xi)s')
    else:
        break
    print('Try again!\n')


spline = cubic_spline(x_values, y_values)
print_cubic_spline(spline, x_values)
draw_graph(spline, x_values)

while True:
    x = float([float(i) for i in input('Enter Interpolation x to calculate: ').split()][0])
    if x >= min(x_values) and x <= max(x_values):
        break
    else:
        print(f'Entered x is not in range of [{min(x_values)}, {max(x_values)}]\n Try again!\n')

print(calculate_interpolation(spline, x_values, x))
