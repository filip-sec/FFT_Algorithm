import numpy as np
import matplotlib.pyplot as plt

# Given points for the first polynomial
points_1 = [(-3, 1), (-1, -1)]

# Given points for the second polynomial
points_2 = [(-1, 0), (2, 1)]

# Construct the coefficient matrices for the systems of equations
A_1 = np.array([[1, -3, 9], [1, -1, 1]])
A_2 = np.array([[1, -1, 1, -1], [1, 2, 4, 8]])

# Construct the constant term vectors for the systems of equations
b_1 = np.array([1, -1])
b_2 = np.array([0, 1])

# Solve the systems of equations
coefficients_1 = np.linalg.lstsq(A_1, b_1, rcond=None)[0]
coefficients_2 = np.linalg.lstsq(A_2, b_2, rcond=None)[0]

# Define polynomial functions
def polynomial_1(x):
    return coefficients_1[0] + coefficients_1[1]*x + coefficients_1[2]*x**2

def polynomial_2(x):
    return coefficients_2[0] + coefficients_2[1]*x + coefficients_2[2]*x**2 + coefficients_2[3]*x**3

# Plotting
x_values = np.linspace(-4, 4, 400)

plt.plot(x_values, polynomial_1(x_values), label=r'$P(x) = \frac{3}{4} x^2 + 2x + \frac{1}{4}$')
plt.plot(x_values, polynomial_2(x_values), label=r'$P(x) = \frac{2}{3} x^3 - x^2 - \frac{2}{3}x + 1$')

# Plot given points
x_1, y_1 = zip(*points_1)
plt.scatter(x_1, y_1, color='red', label='Given Points for 1st Polynomial')

x_2, y_2 = zip(*points_2)
plt.scatter(x_2, y_2, color='blue', label='Given Points for 2nd Polynomial')

plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Plot of Polynomials with Given Points')
plt.legend()
plt.grid(True)
plt.show()
