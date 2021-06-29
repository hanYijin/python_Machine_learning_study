import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge,Lasso
import matplotlib.pyplot as plt

df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
#print(perch_full)

#target 데이터
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)
#print(train_input[:5])
#print(test_input)
poly=PolynomialFeatures()
# poly.fit([[2,3]])
# trans_poly = poly.transform([[2,3]])
# print(trans_poly)
# print(poly.get_feature_names())

# poly.fit(train_input)
# train_poly=poly.transform(train_input)
#['1', 'x0', 'x1', 'x2', 'x0^2', 'x0 x1', 'x0 x2', 'x1^2', 'x1 x2', 'x2^2']
#print(poly.get_feature_names())
# print(train_input[:1])
#print(train_poly[:5])
# test_poly= poly.transform(test_input)

# lr= LinearRegression()
# lr.fit(train_poly,train_target)
# print('훈련 데이터를 넣을때 리니어리그레이션 알고리즘 점수')
# print(lr.score(train_poly,train_target))
# print('테스트 데이터를 넣을때 리니어리그레이션 알고리즘 점수')
# print(lr.score(test_poly,test_target))

#원래는 특성을 변형시킬때 x의 제곱까지지만
#특성을 더 많이 변화시키기 위해서 degree 5로 변경
poly= PolynomialFeatures(degree=5, include_bias=False)
#훈련 데이터의 과대적합의 예
poly.fit(train_input)
train_poly=poly.transform(train_input)
test_poly=poly.transform(test_input)

# print(train_poly.shape)
# print(train_poly[0])
# print(poly.get_feature_names())
#
# lr.fit(train_poly,train_target)
# print('55개의 특성을 가지고...')
# print('훈련 데이터로 리니어모델 점수')
# print(lr.score(train_poly,train_target))
# print('테스트 데이터로 리니어모델 점수')
# print(lr.score(test_poly,test_target))

ss= StandardScaler()
ss.fit(train_poly)
train_scaled= ss.transform(train_poly)
test_scaled =ss.transform(test_poly)
#표준편차
# print(train_scaled[0])
# print(test_scaled[0])

ridge = Ridge()
ridge.fit(train_scaled,train_target)
# print(ridge.score(train_scaled,train_target))
# print(ridge.score(test_scaled,test_target))

train_scores=[]
test_scores=[]
alpha_list=[0.001,0.01, 0.1, 1, 10, 100]

for ele in alpha_list:
    ridge = Ridge(alpha=ele)
    ridge.fit(train_scaled,train_target)
    train= ridge.score(train_scaled,train_target)
    train_scores.append(train)
    test= ridge.score(test_scaled,test_target)
    test_scores.append(test)

# print(train_scores)
# print(test_scores)
print(np.log10(alpha_list))

plt.plot(np.log10(alpha_list),train_scores)
plt.plot(np.log10(alpha_list),test_scores)
plt.xlabel("alpha_list")
plt.ylabel("R2")
plt.show()

train_scores=[]
test_scores=[]
alpha_list=[0.001,0.01, 0.1, 1, 10, 100]

for ele in alpha_list:
    lasso = Lasso(alpha=ele)
    lasso.fit(train_scaled,train_target)
    train= lasso.score(train_scaled,train_target)
    train_scores.append(train)
    test= lasso.score(test_scaled,test_target)
    test_scores.append(test)

# print(train_scores)
# print(test_scores)
print(np.log10(alpha_list))

plt.plot(np.log10(alpha_list),train_scores)
plt.plot(np.log10(alpha_list),test_scores)
plt.xlabel("alpha_list")
plt.ylabel("R2")
plt.show()