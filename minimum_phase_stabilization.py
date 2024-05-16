import math
import matplotlib.pyplot as plt

# Initialize the system
# x1 = 2
# x2 = 2
# x3 = 2

x1 = 20
x2 = 10
x3 = 5

# Controller gains
# k1>0, k2>0, k2**2 > 4*k1
# For higher values of k1 and k2, the system becomes stable for greater range of initial conditions

# k1 = 1
# k2 = 3

k1 = 5
k2 = 50

delta_time = 0.0001

# Initialize lists to store values
x1_values = []
x2_values = []
x3_values = []
x1_dot_values = []
x2_dot_values = []
x3_dot_values = []
y_values = []

# Simulate the system
for i in range(10000):
    # Calculate intermediate variables
    z1 = x1
    z2 = x3 - math.pow(x2, 3)
    z3 = x2 + x3

    b = 1 + 3 * math.pow(x2, 2)
    a = -(math.pow(x1, 2) - x3 + 3 * math.pow(x2, 2)) - (k1 * z1) - (k2 * z2)
    u = a / b

    # Calculate state derivatives
    x1_dot = x3 - math.pow(x2, 3)
    x2_dot = -x2 - u
    x3_dot = math.pow(x1, 2) - x3 + u
    y = x1

    # Update states
    x1 = x1 + x1_dot * delta_time
    x2 = x2 + x2_dot * delta_time
    x3 = x3 + x3_dot * delta_time

    # Print states
    print("x1: ", x1, "x2: ", x2, "x3: ", x3, "y: ", y)

    # Store values
    x1_values.append(x1)
    x2_values.append(x2)
    x3_values.append(x3)
    x1_dot_values.append(x1_dot)
    x2_dot_values.append(x2_dot)
    x3_dot_values.append(x3_dot)
    y_values.append(y)

def plot_values(values, label):
    plt.subplot(3, 3, len(plt.gcf().axes) + 1)
    plt.plot(values, label=label)
    plt.legend()

# Plot values
plt.figure(figsize=(12, 8))

plot_values(x1_values, 'x1')
plot_values(x2_values, 'x2')
plot_values(x3_values, 'x3')
plot_values(x1_dot_values, 'x1_dot')
plot_values(x2_dot_values, 'x2_dot')
plot_values(x3_dot_values, 'x3_dot')
plot_values(y_values, 'y')

plt.show()