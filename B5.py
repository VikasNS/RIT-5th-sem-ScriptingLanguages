from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor

import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv('Housing.csv')
df.drop(['ID'],axis=1,inplace=True)
from matplotlib import pyplot

for i,column in enumerate(df.columns):
    pyplot.subplot(5,3,i+1)
    pyplot.scatter(df[column],df.iloc[:,-1])
    pyplot.xlabel(column)
pyplot.show()

df=(df-df.mean())/df.std()
X=df.iloc[:,:-1]
y=df.iloc[:,-1]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


a=MLPRegressor()
a.fit(X_train,y_train)
print(a.score(X_test,y_test))

