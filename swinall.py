import numpy as np
import matplotlib.pyplot as plt

def elliptic_curve(a, b, x):
    """ Calculate y^2 for the given x on the elliptic curve y^2 = x^3 + ax + b """
    return x**3 + a*x + b

def robust_simplified_L_function(a, x):
    """ A more robust version of the simplified L-function to avoid division by zero """
    return 1 / (1 + abs(a * x**2))

def plot_elliptic_curve(a, b, x_values):
    """ Plot the elliptic curve """
    y_squared = elliptic_curve(a, b, x_values)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, np.sqrt(np.abs(y_squared)), label="y", color="blue")
    plt.plot(x_values, -np.sqrt(np.abs(y_squared)), color="blue")
    plt.title(f"Elliptic Curve y^2 = x^3 + {a}x + {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.show()

# Parameters for the elliptic curve
a, b = -1, 0  # These can be adjusted

# Generate x values
x_values = np.linspace(-2, 2, 400)

# Plot the elliptic curve
plot_elliptic_curve(a, b, x_values)

# Calculate the value of the robust simplified L-function at x = 1
L_value_at_1 = robust_simplified_L_function(a, 1)
print(f"The value of the robust simplified L-function at x = 1 is: {L_value_at_1}")
