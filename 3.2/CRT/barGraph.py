import matplotlib.pyplot as plt
# data to display on plots
x = [1,2,3,4,5,6,7,8]
y = [6,8,17,12,15,23,11,9]

# This will plot a simple bar chart
plt.bar(x, y)

# Title to the plot
plt.title("Bar Chart")

# Adding the legends
plt.legend(["bar"])
plt.show()
