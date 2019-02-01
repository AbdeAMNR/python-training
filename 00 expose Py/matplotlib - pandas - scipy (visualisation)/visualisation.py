import pandas
from matplotlib import pyplot
from scipy import stats

my_data = pandas.read_csv("univariate_linear_regression_dataset.csv")

print("head : ")
print(my_data.head())
print("tail : ")
print(my_data.tail())

X = my_data.iloc[0:len(my_data), 0]
Y = my_data.iloc[0:len(my_data), 1]

pyplot.xlim([0, 25])
pyplot.ylim([0, 25])

pyplot.title("Le diagramme de dispersion de Y en fonction de X")
pyplot.ylabel("L'axe des ordonnees")
pyplot.xlabel("L'axe des abscisses")

pyplot.scatter(X, Y)

# this line allows saving a picture for a scatter
# in this needs to give the path were to save the picture
pyplot.savefig("python.png")

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)


def predict(x):
    return slope * x + intercept


YY = predict(X)
pyplot.plot(X, YY, c='r')
pyplot.show()

print("\n=====================================================")
print("Estimation pour X = 20 : ", predict(20))
print("Coeficient de regression : ", slope)
print("Coeficient de corrélation : ", r_value)
print("Qualité d'ajustement : ", r_value * r_value)
print("=====================================================\n")
