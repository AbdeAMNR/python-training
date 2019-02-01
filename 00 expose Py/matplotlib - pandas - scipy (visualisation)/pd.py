import pandas

tbl = pandas.read_table('univariate_linear_regression_dataset.csv', sep=',', header=None)
print(tbl.head())
print(tbl.tail())
x, y = tbl.shape
print(y,'dfdddddddddddddddddddddddddddddddddddddd')
print('----------------------------')
print(tbl[0])
