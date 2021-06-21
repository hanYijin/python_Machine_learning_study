'''
분류는
학습데이터와 예측데이터를 분류
회귀
물고기 데이터에서 가로의 길이와 세로의 길이를 학습시켜 무게를 예측하는 것
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor # K_최근접 이웃 회귀 라이브러리
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

# plt.scatter(perch_length,perch_weight)
# plt.xlabel('lenght')
# plt.ylabel('weight')
# plt.show()
# plt.savefig('static/perch_gra.png')
# plt.close()

train_date, test_date, train_target, test_target= train_test_split(perch_length,perch_weight,random_state=42)
# print("학습할 데이터 크기: ",train_date.shape)
# print("테스트할 데이터 크기: ", test_date.shape)
# print(train_date[:5])
# print(test_date[:5])
#print(train_target)
train_date = train_date.reshape(-1,1) #1열로 된 2차원 배열 반환
test_date = test_date.reshape(-1,1)

# print("학습할 데이터 크기: ",train_date.shape)
# print("테스트할 데이터 크기: ", test_date.shape)
# print(train_date[:5])
# print(test_date[:5])
kn= KNeighborsRegressor()
print(kn)
test= np.array([50,60,70]).reshape(-1,1)
kn.fit(train_date,train_target) #2차원 배열로 학습
predictvalue= kn.predict(test) #예측값 역시 2차원 배열로 예측
print("예측되는 값: ",predictvalue)
# plt.scatter(test,predictvalue)
# plt.show()
x= np.arange(5,45).reshape(-1,1)
y= np.arange(45,85).reshape(-1,1)
plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel('xxx')
plt.ylabel('yyy')
plt.show()

# for n in [1,5,10]:
#  plt.scatter(perch_length,perch_weight)
#  plt.plot(x,)
#  plt.xlabel('lenght')
#  plt.ylabel('weight')