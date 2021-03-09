import pandas
from sklearn.linear_model import LinearRegression

user = input('enter the price of iphone you want to know the predicted price: ')

data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
ode = LinearRegression()



ode.fit(data[['version']], data[['price']])

print(ode.predict([[user]]))
