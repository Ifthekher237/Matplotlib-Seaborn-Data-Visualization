
from pylab import plot, show, legend
'''
#simply plotting points and connecting them by line
x_numbers = [2, 3, 1]
y_numbers = [4, 6, 2]

plot(x_numbers, y_numbers, "o")
show()
'''

'''
#When you use plot() on a single list, those numbers are 
#automatically plotted on the y-axis. The corresponding values on the 
#x-axis are filled in as the positions of each value in the list.

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 
            55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

plot(nyc_temp,marker="o")

show()
'''

'''
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 
            55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years=range(2000, 2013)

plot(years, nyc_temp, marker="o")
show()
'''

