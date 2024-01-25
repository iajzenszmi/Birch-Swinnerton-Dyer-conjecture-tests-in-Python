from sympy import symbols, Eq, solve
from fractions import Fraction

# Define the symbols
x, y = symbols('x y')

# Define an elliptic curve, for example, y^2 = x^3 - x
curve_equation = Eq(y**2, x**3 - x)

# Function to find rational points on the elliptic curve
def find_rational_points(curve, search_range):
    points = []
    for x_val in range(-search_range, search_range + 1):
        # Substitute x in the curve equation
        substituted_eq = curve.subs(x, x_val)
        # Try to solve for y
        y_solutions = solve(substituted_eq, y)
        # Check if solutions are rational
        for sol in y_solutions:
            if sol.is_rational:
                points.append((Fraction(x_val), sol))
    print("points ",points)
    print("y_solutions ",y_solutions)
    return points

# Search for rational points in a specified range
rational_points = find_rational_points(curve_equation, 5)  # Searching in the range -5 to 5
rational_points


