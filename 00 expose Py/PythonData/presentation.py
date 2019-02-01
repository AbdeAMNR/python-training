import numpy
from matplotlib import pyplot

data = numpy.genfromtxt('faithful.csv', delimiter=',', skip_header=1)

pyplot.plot(data[:, 1], data[:, 2], '.b', label='Observations')

pyplot.xlabel('Axe des X')
pyplot.ylabel('Axe des Y')
# pyplot.ylim([0,100])
pyplot.legend(loc='best')

mx = numpy.mean(data[:, 1])
my = numpy.mean(data[:, 2])

coef = numpy.polyfit(data[:, 1], data[:, 2], 1)

plot_x = numpy.linspace(1.5, 5.5)
plot_y = coef[0] * plot_x + coef[1]

pyplot.plot(plot_x, plot_y, ':r', label="Linear Regrission")

rMatrix = numpy.corrcoef(data[:, 1], data[:, 2])
r = rMatrix[0][1]
print(r)

pyplot.show()