import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# tomato=pd.read_csv('./data_csv/result.csv')
# print(tomato.head())
# print(tomato.info())
# print(tomato.describe())# 데이터에 0값이 있음을 확인
# print('------------데이터 결측값 평균으로 대체하기위한 처리과정------------')
# print('1. 0 값 NaN 처리')
# tomato=tomato.replace(0,np.NaN)# 0값을 NaN으로 교체
# print(tomato)
# print(tomato.info())
# print(tomato.describe())
# print('2. 결측값 평균값 대체')
# tomato.fillna(tomato.mean(),inplace=True) #fillna()로 결측값 평균값으로 대체
# print(tomato)
# print(tomato.describe())
# tomato.to_csv('./data_csv/tomato.csv',encoding='UTF_8')
tomato=pd.read_csv('./data_csv/tomato.csv')
# print(tomato.describe())
data=tomato[['생장길이', '화방높이', '줄기굵기', '잎길이(엽장)', '착과군', '개화군']].to_numpy()
target = tomato['열매수'].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2,random_state=42)
print(train_input.shape,test_input.shape)

ss= StandardScaler()
ss.fit(train_input)
train_scaled=ss.transform(train_input)
test_scaled=ss.transform(test_input)


print(train_scaled[:5])
print(test_scaled[:5])
lr=LogisticRegression()
lr.fit(train_input,train_target)
# print(lr.score(train_scaled,train_target))
print(lr.score(test_scaled,test_target))

