#https://www.youtube.com/watch?v=iedmZlFxjfA  ==> by codebasics

import matplotlib.pyplot as plt
import numpy as np

# Number of steps I walked during the past week
me = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
my_wife=[2312,4000,5341,3333,1321,7123,2312]
# Corresponding days
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

#plt.bar(x_val, y_val) ei method er x_val/y_val e text value use kora jabe na, bt amader
#x_val gulo text. so amra 1st e text value gulo use na kore number use kore graph 
#draw korbo, then plt.xticks() use kre oi number gulo k text value dara replace kre dibo
position=np.arange(len(labels))

#position-.2 ==> returns an array where each value is subtracted from .2. if we used 
#usual range() funciton, then this would raise error
plt.bar(position-.2, me, width=.4, label="ME")
plt.bar(position+.2,my_wife, width=.4, label="MY_WIFE")
plt.xticks(position,labels)

plt.title("number of steps walked")
plt.legend()  #another way of plotting legend
plt.show()