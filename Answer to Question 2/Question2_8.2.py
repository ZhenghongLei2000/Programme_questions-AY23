import numpy as np

# Define the rate constants
k1 = 100/10**6/60 # 100/µM/min -> 1/min
k2 = 600 # 1/min
k3 = 150 # 1/min

# Define the initial concentrations
E = [1 * (10**-6)] # 1 µM
S = [10 * (10**-6)] # 10 µM
ES = [0]
P = [0]
x = [E, S, ES, P]

# Define the step size (time step) and the number of steps
h = 0.01 # step size in minutes
num_steps = 1000

# Define the function to calculate the derivatives
def dxdt(E, S, ES, P, k1, k2, k3):
    dEdt = -k1 * E * S + k2 * ES
    dSdt = -k1 * E * S + k2 * ES
    dESdt = k1 * E * S - (k2 + k3) * ES
    dPdt = k3 * ES
    return [dEdt, dSdt, dESdt, dPdt]

# Define the fourth-order Runge-Kutta method
def runge_kutta_4(dxdt, x, t, h, k1, k2, k3):
    k1 = dxdt(x, t, k1, k2, k3)
    k2 = dxdt(x + 0.5 * h * k1, t + 0.5 * h, k1, k2, k3)
    k3 = dxdt(x + 0.5 * h * k2, t + 0.5 * h, k1, k2, k3)
    k4 = dxdt(x + h * k3, t + h, k1, k2, k3)
    return x + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

# Perform the simulation
for i in range(num_steps):
    t = i * h
    E.append(runge_kutta_4(dxdt, E[-1], t, h, k1, k2, k3)[0])
    S.append(runge_kutta_4(dxdt, S[-1], t, h, k1, k2, k3)[1])
    ES.append(runge_kutta_4(dxdt, ES[-1], t, h, k1, k2, k3)[2])
    P.append(runge_kutta_4(dxdt, P[-1], t, h, k1, k2, k3)[3])

# Print the concentration at the final time point
print("E = ", E[-1], "S = ", S[-1], "ES = ", ES[-1], "P = ", P[-1])
