import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
#결정트리
wine = pd.read_csv('https://bit.ly/wine_csv_data')
# print(wine.head())
#로지스틱 회귀로 와인 분류
# print(wine.info())
# print(wine.describe()) #데이터 행수, 평균,표준편차,최소값,...
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)
print(train_input.shape, test_input.shape)#학습데이터와 테스트데이터

ss= StandardScaler()
#각 feature의 평균을 0, 분산을 1로 변경합니다. 모든 특성들이 같은 스케일을 갖게 됩니다.
ss.fit(train_input)
train_scaled= ss.transform(train_input)
test_scaled=ss.transform(test_input)
#fit():  평균 𝜇과  표준편차 𝜎를 계산
#transform():정규화/표준화,
print(train_scaled[:5])
print(test_scaled[:5])
#로지스틱회귀
lr=LogisticRegression()
lr.fit(train_scaled,train_target)

train_score=lr.score(train_scaled,train_target)
test_score=lr.score(test_scaled,test_target)
print('로지스틱',train_score)
print('로지스틱 예측값',test_score)

#결정트리
dtc=DecisionTreeClassifier()
dtc.fit(train_scaled,train_target)
trainscore=dtc.score(train_scaled,train_target)
testscore=dtc.score(test_scaled,test_target)
print('결정트리',trainscore)
print('결정트리예측값',testscore)

# plt.figure(figsize=(10,7))#사이즈 10행 7열
# plot_tree(dtc)
# plt.show()
plt.figure(figsize=(10,7))
plot_tree(dtc, max_depth=2, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
#하이퍼 파라미터 :max_depth=1 깊이값 설정
plt.show()
#Gini Impurity Measure(지니 불순도)
#변수 중요도
# (와인의 당도에 따른 화이트 와인 레드와인 분류)
print(dtc.feature_importances_)
'''
    max_depth
    impurity_decrease
    하이퍼파라미터 설정하여 예측점수 높여줌
    지니 불순도 계수 조정
'''