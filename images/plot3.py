import numpy as np
import matplotlib.pyplot as plt

# Define functions A(x), B(x), and C(x)
def A_x(x):
    return (x + 1) ** 2

def B_x(x):
    return (x - 1) ** 2

def C_x(x):
    return A_x(x) * B_x(x)

# Points for A(x) and B(x)
points_A = [(-2, 1), (-1, 0), (0, 1), (1, 4), (2, 9)]
points_B = [(-2, 9), (-1, 4), (0, 1), (1, 0), (2, 1)]

# Generate x values
x_values = np.linspace(-2, 2, 100)

# Generate y values for A(x), B(x), and C(x)
y_A = A_x(x_values)
y_B = B_x(x_values)
y_C = C_x(x_values)

# Extract x and y values from the points for A(x) and B(x)
x_points_A, y_points_A = zip(*points_A)
x_points_B, y_points_B = zip(*points_B)

# Plot the functions
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_A, label='$A(x)$')
plt.plot(x_values, y_B, label='$B(x)$', linestyle='--')
plt.plot(x_values, y_C, label='$C(x) = A(x) \\times B(x)$', linestyle='-.') # Plot C(x)

# Plot the points for A(x) and B(x)
plt.scatter(x_points_A, y_points_A, color='red', label='Points for $A(x)$')
plt.scatter(x_points_B, y_points_B, color='blue', label='Points for $B(x)$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $A(x)$, $B(x)$, and $C(x)$')
plt.legend()
plt.grid(True)
plt.show()
