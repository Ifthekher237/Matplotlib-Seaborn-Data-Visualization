import matplotlib.pyplot as plt

x=[1,2,3]
y=[4,5,6]

#plt.subplot(nrows, ncolumn, nsubplots)

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("plot1")

plt.subplot(2,2,2)
plt.plot(x,y)
plt.title("plot2")

plt.subplot(2,2,3)
plt.plot(x,y)
plt.title("plot3")

plt.subplot(2,2,4)
plt.plot(x,y)
plt.title("plot4")

plt.suptitle("All plots")
plt.show()