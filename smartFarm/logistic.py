import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
import xgboost

tomato = pd.read_csv('./data_csv/tomato.csv')
tomato_target = tomato['열매수'].to_numpy()
# 독립변수
tomato_input = tomato[['생장길이', '화방높이', '줄기굵기', '잎길이(엽장)','착과군', '개화군']].to_numpy()
# print(tomato_input)

tranin_input, test_input, train_target, test_target = train_test_split(tomato_input, tomato_target, random_state=42)

ss = StandardScaler()
ss.fit(tranin_input)
train_scaled = ss.transform(tranin_input)
test_scaled = ss.transform(test_input)
print(train_scaled[:5])
train_target=round(train_target,3)
train_scaled=round(train_scaled,3)
test_scaled=round(test_scaled,3)
test_target=round(test_target,3)
print(train_scaled[:5])
print(train_target.dtype)
lr = LinearRegression()
lr.fit(train_scaled, train_target)

score = lr.score(test_scaled, test_target)
print('LinearRegression: ',score)
print(lr.coef_, lr.intercept_)

# knr = KNeighborsRegressor()
# knr.fit(train_scaled, train_target)
#
# score = knr.score(test_scaled, test_target)
# print(score)
#
# dtr = DecisionTreeRegressor(max_depth=4)
# dtr.fit(train_scaled, train_target)
#
# score = dtr.score(test_scaled, test_target)
# print(score)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)

print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))



# rfr = RandomForestRegressor()
# rfr.fit(train_scaled, train_target)
#
# score = rfr.score(test_scaled, test_target)
# print(score)
#
# xgb_model = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=7)
# xgb_model.fit(train_scaled,train_target)
# score = xgb_model.score(test_scaled, test_target)
# print(score)
# print(train_scaled)

# z = np.arange(-5, 5, 0.1)
# phi = 1 / (1 + np.exp(-z))
# plt.plot(z, phi)
# plt.xlabel('z')
# plt.ylabel('phi')
# plt.show()


# df1= pd.DataFrame(tomato_input).T
#
# print(tomato.corr())