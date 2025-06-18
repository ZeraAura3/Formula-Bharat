import numpy as np
from scipy.optimize import fsolve
from math import sin, cos, radians

# Define variables with appropriate units
t_d = 20 * 0.0254  # 20 inches to meters
t_w = 8 * 0.0254   # 8 inches to meters
L = 1.524          # meters
W = 1.27           # meters
beta = radians(20.457)  # degrees to radians
del_i = radians(40)     # degrees to radians
del_o = radians(27.296) # degrees to radians
p = 0.273          # meters
r = 0.0635         # meters
x = 0.0753         # meters
B = 1.137          # meters

# Define the system of equations
def equations(vars):
    y, q, d = vars
    eq1 = y**2 - ((B/2 - (p/2 + r - q) - x * sin(del_i + beta))**2 + (d - x * cos(del_i + beta))**2)
    eq2 = y**2 - ((B/2 - (p/2 + r + q) + x * sin(del_o - beta))**2 + (d - x * cos(del_o - beta))**2)
    eq3 = y**2 - ((B/2 - p/2 - r - x * sin(beta))**2 + (d - x * cos(beta))**2)
    return [eq1, eq2, eq3]

# Initial guesses for y, q, d
initial_guess = [0.5, 0.1, 0.5]

# Solve the system of equations using fsolve
solution = fsolve(equations, initial_guess)

# Extract the results
y, q, d = solution

# Print the results
print(f"y = {y:.4f} meters")
print(f"q = {q:.4f} meters")
print(f"d = {d:.4f} meters")

print("beta = ", beta)
print("ठ_i= ", del_i)
print("ठ_o= ", del_o)
