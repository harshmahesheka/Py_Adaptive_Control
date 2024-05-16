import math
import matplotlib.pyplot as plt

def plot_values(values, label, subplot_position):
    """
    Plot the given values with the specified label in the given subplot position.
    """
    plt.subplot(subplot_position)
    plt.plot(values, label=label)
    plt.legend()

# Initializing the parameters
x = 1000
theta_cap = 1
theta = 1

x_values = []
theta_cap_values = []
x_dot_values = []
theta_cap_dot_values = []

delta_time = 0.0001

for i in range(50000):

    u = -(theta_cap + math.sqrt(math.pow(theta_cap, 2) + 1)) * x

    # Guessed simple adaptive control law
    # u = -(theta_cap) * x
    
    # To check speed of convergence
    # if abs(x) < 0.01:
    #     print(i)
    #     break

    x_dot = theta * x + u
    theta_cap_dot = math.pow(x, 2)

    x = x + x_dot * delta_time
    theta_cap = theta_cap + theta_cap_dot * delta_time

    x_values.append(x)
    theta_cap_values.append(theta_cap)
    x_dot_values.append(x_dot)
    theta_cap_dot_values.append(theta_cap_dot)
    
    print("x: ", x, "theta_cap: ", theta_cap, "x_dot: ", x_dot, "theta_cap_dot: ", theta_cap_dot)

# Plot values
plt.figure(figsize=(12, 8))

plot_values(x_values, 'x', 221)
plot_values(theta_cap_values, 'theta_cap', 222)
plot_values(x_dot_values, 'x_dot', 223)
plot_values(theta_cap_dot_values, 'theta_cap_dot', 224)

plt.show()
