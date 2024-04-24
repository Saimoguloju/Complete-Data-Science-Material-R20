import matplotlib.pyplot as plt
# data to display on plots
x = [3, 1, 3]
y = [3, 2, 1]

# This will plot a simple line chart
# with elements of x as x axis and y
# as y axis
plt.plot(x, y)
plt.title("Line Chart")

# Adding the legends
plt.legend(["Line"])
plt.show()
