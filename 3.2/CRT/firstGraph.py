import matplotlib.pyplot as plt

# initializing the data
x = [1,2,3,4,5]
y = [85,87,83,86,85]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Performance report")

# Adding the labels
plt.ylabel("percentage of marks")
plt.xlabel("Sem number")
plt.show()
