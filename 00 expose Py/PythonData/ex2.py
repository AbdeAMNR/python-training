import pandas
import seaborn
from matplotlib import pyplot
from statsmodels.formula.api import ols

df = pandas.read_csv('faithful.csv', delimiter=',')
df.head()
df.isnull().any()
df.dtypes
df.describe()

fig = pyplot.figure(figsize=(12, 6))
sqft = fig.add_subplot(121)
cost = fig.add_subplot(122)

sqft.hist(df.sqft_living, bins=80)
sqft.set_xlabel('Ft^2')
sqft.set_title("Histogram de squer footage")

cost.hist(df.price, bins=80)
cost.set_xlabel('Prix ($)')
cost.set_title("Histogram de prix")

pyplot.show()

m = ols('price ~ sqft_living', df).fit()
print(m.summary())

m = ols('price ~ sqft_living + bedrooms + grade + condition', df).fit()
print(m.summary())

seaborn.jointplot(x="sqft_living", y="price", data=df, kind='reg', size=7)
pyplot.show()
