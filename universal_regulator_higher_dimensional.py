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
a = 1
b = 2
c_T = 3
d = 4
A = -5

# Initializing the state variables
y = 1
z = 2
k = 1

delta_time = 0.0001

# Initialize lists to store values
y_values = []
z_values = []
k_values = []
y_dot_values = []
z_dot_values = []
k_dot_values = []

for i in range(10000):
    # Calculate control input
    N_k = k * math.cos(k)
    u = -N_k * k * y
    
    # Calculate state derivatives
    y_dot = a * y + b * u + c_T * z
    z_dot = A * z + d * y
    k_dot = math.pow(y, 2)

    # Update states using Euler's method
    y = y + y_dot * delta_time
    z = z + z_dot * delta_time
    k = k + k_dot * delta_time

    # Print state variables and derivatives
    print("y: ", y, "z: ", z, "k: ", k, "y_dot: ", y_dot, "z_dot: ", z_dot, "k_dot: ", k_dot)

    # Store values
    y_values.append(y)
    z_values.append(z)
    k_values.append(k)
    y_dot_values.append(y_dot)
    z_dot_values.append(z_dot)
    k_dot_values.append(k_dot)

# Plot values
plt.figure(figsize=(12, 8))

plot_values(y_values, 'y', 321)
plot_values(z_values, 'z', 322)
plot_values(k_values, 'k', 323)
plot_values(y_dot_values, 'y_dot', 324)
plot_values(z_dot_values, 'z_dot', 325)
plot_values(k_dot_values, 'k_dot', 326)

plt.show()