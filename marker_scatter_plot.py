# marker_scatter_plot.py

# import the required library
import matplotlib.pyplot as plt

# h and w data
h = [165, 173, 172, 188, 191, 189, 157, 167, 184, 189]
w = [55, 60, 72, 70, 96, 84, 60, 68, 98, 95]

# plot a scatter plot
plt.scatter(h, w, marker="v", s=75)

# set the axis lables names
plt.xlabel("weight (w) in Kg")
plt.ylabel("height (h) in cm")

# set the title of the chart name
plt.title("Scatter plot where marker change")
plt.show()