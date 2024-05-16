import math
import matplotlib.pyplot as plt

def plot_values(values, label, subplot_position):
    """
    Plot the given values with the specified label in the specified subplot position.
    """
    plt.subplot(subplot_position)
    plt.plot(values, label=label)
    plt.legend()

# Initializing the parameters
a = 10
b = 1

# Initializing the state variables
x = 10
k = 10
delta_time = 0.0001

# Initialize lists to store values
x_values = []
x_dot_values = []
k_values = []
k_dot_values = []

for i in range(10000):
    # Calculate control input
    u = -k * x

    # Calculate state derivatives
    x_dot = a * x + b * u
    k_dot = math.pow(x, 2)

    # Update states
    x = x + x_dot * delta_time
    k = k + k_dot * delta_time

    # Print current state values
    print("x: ", x, "x_dot: ", x_dot, "k: ", k, "k_dot: ", k_dot)

    # Store values for plotting
    x_values.append(x)
    x_dot_values.append(x_dot)
    k_values.append(k)
    k_dot_values.append(k_dot)

# Plot values
plt.figure(figsize=(12, 8))

plot_values(x_values, 'x', 321)
plot_values(x_dot_values, 'x_dot', 322)
plot_values(k_values, 'k', 323)
plot_values(k_dot_values, 'k_dot', 324)

plt.show()