import matplotlib.pyplot as plt
# data to display on plots
x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]

# This will plot a simple scatter chart
plt.scatter(x, y)

# Adding legend to the plot
plt.legend("A")

# Title to the plot
plt.title("Scatter chart")
plt.show()
