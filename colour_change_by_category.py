# colour_change_by_category.py

# import the required library
import matplotlib.pyplot as plt

# h and w data gather from two country
h = [165, 173, 172, 188, 191, 189, 157, 167, 184, 189]
w = [55, 60, 72, 70, 96, 84, 60, 68, 98, 95]

# set the country name 1 or 2 which shows the height or weight
# data belongs to which country
country_category = ['country_2', 'country_2', 'country_1',
                    'country_1', 'country_1', 'country_1',
           'country_2', 'country_2', 'country_1', 'country_2']

# color mapping
colours = {'country_1':'orange', 'country_2':'blue'}
colour_list = [colours[i] for i in country_category]

# print the colour list
print(colour_list)

# plot a scatter plot
plt.scatter(h, w, marker="v", s=75,c=colour_list)

# set the axis lables names
plt.xlabel("weight (w) in Kg")
plt.ylabel("height (h) in cm")

# set the title of the chart name
plt.title("Scatter plot colour change for category wise")
plt.show()