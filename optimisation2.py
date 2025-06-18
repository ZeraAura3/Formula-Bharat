import numpy as np
from scipy.optimize import fsolve
from math import sin, cos, radians
from matplotlib import pyplot as plt

# Define variables with appropriate units
change = np.arange(0, 1, 0.1)  # 0 to 1 in steps of 0.1
tie_rod = []
rack_travel = []
distance = []
for i in change:
    t_d = 20 * 0.0254  # 20 inches to meters
    t_w = 8 * 0.0254   # 8 inches to meters
    tr = 3
    L = 1.550          # meters
    W = 1.250          # meters
    beta = 0.346      # degrees to radians # 20.457 degrees old book
    # del_i = 0.6526    # degrees to radians # 40 degrees old book
    del_i = L/(tr - W/2)   # near about 28 for old
    # del_o = 0.4275    # degrees to radians # 27.296 degrees old book
    del_o = L/(tr + W/2)   # near about 26 for old
    p = 0.428           # meters  Length of rack casing
    r = 0.031          # meters  rack ball joint radius
    steering_arm = 0.114          # meters
    B = 1.119          # meters

    # near about 71 ackerman percentage

    # y = tie rod length
    # q = rack travel distance
    # d = Distance between front axis and rack center axis

    # Define the system of equations
    def equations(vars):
        y, q, d = vars
        eq1 = y**2 - ((B/2 - (p/2 + r - q) - steering_arm * sin(del_i + beta))**2 + (d - steering_arm * cos(del_i + beta))**2)
        eq2 = y**2 - ((B/2 - (p/2 + r + q) + steering_arm * sin(del_o - beta))**2 + (d - steering_arm * cos(del_o - beta))**2)
        eq3 = y**2 - ((B/2 - p/2 - r - steering_arm * sin(beta))**2 + (d - steering_arm * cos(beta))**2)
        return [eq1, eq2, eq3]

    # Initial guesses for y, q, d
    initial_guess = [0.5, 0.1, 0.5]

    # Solve the system of equations using fsolve
    solution = fsolve(equations, initial_guess)

    # Esteering_armtract the results
    y, q, d = solution

    # Print the results
    print(f"y = {y:.4f} meters")
    print(f"q = {q:.4f} meters")
    print(f"d = {d:.4f} meters")
    tie_rod.append(y)
    rack_travel.append(q)
    distance.append(d)

plt.plot(i, tie_rod, label='Tie rod length')
plt.plot(i, rack_travel, label='Rack travel distance')
plt.plot(i, distance, label='Distance between front axis and rack center axis')
plt.legend()
plt.show()


# ground clearance
# why wishbone parallel
# how front wishbone and rear wishbones are generally connected to chasis