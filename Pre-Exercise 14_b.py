import matplotlib.pyplot as plt
x = [5, 10, 15, 20, 25, 30] # for x-axis
y = [96, 83, 78, 60, 52, 30] # for y-axis
plt.scatter(x, y)
plt.rcParams.update ({"figure.figsize":(10,8), "figure.dpi":100})
plt.title("Pre-Exercise 14.b. (Scatter Plot)")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.show()