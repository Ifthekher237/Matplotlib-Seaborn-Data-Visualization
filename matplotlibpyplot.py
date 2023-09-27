#all the methods that we learned about when using pylab will work the same way 
#with pyplot.

import matplotlib.pyplot as plt

#plotting 2 or more lines in a graph
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 
                72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
#nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 
#                77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
#nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 
#                78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months=range(1,13)

plt.plot(months, nyc_temp_2000, marker="o")
plt.legend([2000],loc='upper left')
plt.title("Average Monthly Temperature in NYC")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.axis(ymin=0)
plt.savefig("mygraph.png")
#plt.show()
