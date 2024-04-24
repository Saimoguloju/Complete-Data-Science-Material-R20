x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")
