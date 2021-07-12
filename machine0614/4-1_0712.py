import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split #훈련데이터와 테스트데이터 나누기
from sklearn.neighbors import KNeighborsClassifier # 이웃알고리즘 분류
from sklearn.preprocessing import StandardScaler # 표준점수 구하는 클래스
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression #로직스틱 분류 모델 가져오기

fish = pd.read_csv('https://bit.ly/fish_csv_data')
print(fish.head())

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
print(fish_input[:5])
fish_target= fish['Species'].to_numpy()
print(fish_target[:5])

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

knc=KNeighborsClassifier(n_neighbors=3)
ss= StandardScaler()
ss.fit(train_input)
train_scaled= ss.transform(train_input)
test_scaled= ss.transform(test_input)
knc.fit(train_scaled,train_target)
예측확률= knc.predict_proba(test_scaled[:5])
점수 = knc.score(test_scaled,test_target)
print(np.round(예측확률,decimals=3))
print(점수)

#이진 분류 처리
#불리언 인덱싱
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

lr= LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)
로지스틱확률=lr.predict_proba(train_bream_smelt[:5])
print(로지스틱확률)
#0는 Bream , 1은 smelt
z=lr.decision_function(train_bream_smelt[:5])
print('z=======================')
print(z)

from scipy.special import expit
print('시그모이드')
print(expit(z))



# plt.xlabel('Weight')
# plt.xlabel('Length')
# plt.scatter(fish['Weight'].to_numpy()[:5],fish['Length'].to_numpy()[:5],c='b')
# plt.scatter(fish['Weight'].to_numpy()[5:10],fish['Length'].to_numpy()[5:10],c='r')
# plt.show()
#이진 분류
#z= decision_function
#expit(z) => 확률(시그모이드)
#predict_proba->확률

#다중분류
#z=d