import matplotlib.pyplot as plt

# Original x-values and corresponding y-values
x_values = [360, 480, 720, 864, 1080]
y_values = [10, 20, 15, 25, 30]

# Create evenly spaced values for plotting
evenly_spaced_x = range(len(x_values))

# Plot using the evenly spaced x-values
plt.plot(evenly_spaced_x, y_values, marker='o')

# Replace the x-ticks with the original values
plt.xticks(evenly_spaced_x, x_values)

# Add labels and title
plt.xlabel("Resolution")
plt.ylabel("Performance")
plt.title("Evenly Spaced X-Axis")

# Show the plot
plt.show()
