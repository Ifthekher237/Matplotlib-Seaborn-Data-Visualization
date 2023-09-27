#Anscombe’s Quartet—Four Different Data Sets with Almost Identical
#Statistical Measures
#but they have different scatter plot.
#the main motive of this program is to show why data visualization is why important
import matplotlib.pyplot as plt
import statistics


x1=[10,8,13,9,11,14,6,4,12,7,5]
y1=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2=[10,8,13,9,11,14,6,4,12,7,5]
y2=[9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]

x3=[10,8,13,9,11,14,6,4,12,7,5]
y3=[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

x4=[8,8,8,8,8,8,8,19,8,8,8]
y4=[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89]

#this lambda function takes a list & round every number to 2 decimal places and
#then return a list using list comprehesion
rounding=lambda list: [round(x, 2) for x in list]

means_of_all_x=[statistics.mean(x1), statistics.mean(x2), statistics.mean(x3), statistics.mean(x4)]
means_of_all_y=[statistics.mean(y1), statistics.mean(y2), statistics.mean(y3), statistics.mean(y4)]

stdev_of_all_x=[statistics.stdev(x1), statistics.stdev(x2), statistics.stdev(x3), statistics.stdev(x4)]
stdev_of_all_y=[statistics.stdev(y1), statistics.stdev(y2), statistics.stdev(y3), statistics.stdev(y4)]

print("Means of all x: {}\nMeans of all y: {}\nSD of all x: {}\nSD of all y: {}".format(rounding(means_of_all_x), rounding(means_of_all_y), rounding(stdev_of_all_x), rounding(stdev_of_all_y)))

plt.subplot(2,2,1)
plt.scatter(x1, y1)
plt.xlabel("x1")
plt.ylabel("y1")

plt.subplot(2,2,2)
plt.scatter(x2, y2)
plt.xlabel("x2")
plt.ylabel("y2")

plt.subplot(2,2,3)
plt.scatter(x3, y3)
plt.xlabel("x3")
plt.ylabel("y3")

plt.subplot(2,2,4)
plt.scatter(x4, y4)
plt.xlabel("x4")
plt.ylabel("y4")
plt.show()