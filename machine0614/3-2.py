from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import matplotlib.pyplot as plt
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

train_input, test_input,train_target, test_target=train_test_split(perch_length,perch_weight,random_state=42)
train_input=train_input.reshape(-1,1)
test_input=test_input.reshape(-1,1)

#객체 생성
lr= LinearRegression()
lr.fit(train_input,train_target)
lrprevalue=lr.predict([[50]])
print('lrprevalue 선형회귀 예측 결과',lrprevalue)

kr=KNeighborsRegressor(n_neighbors=3)
kr.fit(train_input,train_target)
krprevalue= kr.predict([[50]])
print('krprevalue K-최근접 이웃',krprevalue)

print(lr.coef_,lr.intercept_)
# y= ax+b
# a=39.01714496 b=-709.0186449535474

# 선형 회귀 그래프
# # plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
# plt.scatter(train_input,train_target)
# plt.xlabel('lenght')
# plt.ylabel('weight')
#plt.show()
#가중치(계수, 기울기 파라미터 W) : lr.coef_
#편향(절편 파라미터 b) : lr.intercept_


# 다향 만들기

train_ploy= np.column_stack((train_input**2,train_input))
test_ploy= np.column_stack((test_input**2, test_input))

# print(train_ploy.shape)
# print(test_ploy.shape)
#
# print(train_ploy[:5])
# print(test_ploy[:5])

lr.fit(train_ploy,train_target)
train_score=lr.score(train_ploy,train_target)
test_score=lr.score(test_ploy,test_target)
print(train_score)
print(test_score)

print(lr.coef_)
print(lr.intercept_)
point=np.arange(15,50)
#다항 회귀 그래프
#plt.plot(point, 1.01433211*point**2+ -21.55792498*point+116.0502107827827])
plt.plot(point,lr.coef_[0]*point**2+lr.coef_[1]*point+lr.intercept_)
plt.scatter(train_input,train_target)
plt.xlabel('lenght')
plt.ylabel('weight')
plt.show()