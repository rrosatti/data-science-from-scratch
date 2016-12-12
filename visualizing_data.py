from matplotlib import pyplot as plt

# ------------------------------ Line Chart ------------------------------
'''
years = ['1970', '1980', '1990', '2000', '2010']
gdp = ['300.4', '512.7', '770.5', '998.9', '1240.6']

# Line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')

# add a title
plt.title('Nominal GDP')

# add label to be the y-axis
plt.ylabel('Billions of $')
plt.show()
'''

# ------------------------------ Bar Chart ------------------------------
'''
movies = ['Annie Hall', 'Ben Hur', 'Casablanca', 'Gandhi']
num_oscars = [5, 11, 4, 1]

# bars are by default width 0.8, so we'll add more 0.1 to the left coordinates, so that each bar are centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel('# of Academy Awards')
plt.title('My Favorite Movies')

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show() 
'''

# ------------------------------ Line Charts (more than one call to plt.plot) ------------------------------
'''
variance = [1, 2, 4, 8, 16, 36, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# making multiple calls to plt.plot
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

# loc=9 means 'top center'
plt.legend(loc=9)
plt.xlabel('model complexity')
plt.title('The Bias-Variance Tradeoff')
plt.show()
'''

# ------------------------------ Scatterplots ------------------------------

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
	plt.annotate(label, 
		xy=(friend_count, minute_count), # put the label with its point
		xytext=(5, -5),					 # but slightly offset
		textcoords='offset points')

plt.title('Daily Minutes vs Number of Friends')
plt.xlabel('# of Friends')
plt.ylabel('daily minutes spent on the site')
plt.show()

