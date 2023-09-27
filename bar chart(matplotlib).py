#https://www.youtube.com/watch?v=iedmZlFxjfA  ==> by codebasics

import matplotlib.pyplot as plt


# Number of steps I walked during the past week
steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]

# Corresponding days
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


#number of bars to be printed
num_bars=len(labels)

#plt.bar(x_val, y_val) ei method er x_val/y_val e text value use kora jabe na, bt amader
#x_val gulo text. so amra 1st e text value gulo use na kore number use kore graph 
#draw korbo, then plt.xticks() use kre oi number gulo k text value dara replace kre dibo

position=range(num_bars)

plt.bar(position, steps, label="ME")
plt.xticks(position,labels)

plt.title("number of steps walked")
plt.legend()  #another way of plotting legend
plt.show()