import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values from 0 to 4π
x = np.linspace(0, 4 * np.pi, 1000)

# Calculate the corresponding y values for the sine and cosine curves
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a plot
plt.figure(figsize=(8, 6))

# Plot the sine curve
plt.plot(x, y_sin, label='Sine Curve')

# Plot the cosine curve
plt.plot(x, y_cos, label='Cosine Curve')

# Set title and labels
plt.title('Sine and Cosine Curves')
plt.xlabel('x')
plt.ylabel('y')

# Add legend
plt.legend()

# Display grid
plt.grid(True)

# Display the plot
plt.show()