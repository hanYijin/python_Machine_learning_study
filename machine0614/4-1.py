import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
fish = pd.read_csv('https://bit.ly/fish_csv_data')
# print(fish.head())

# 물고기 종 (Species)가 target
# Weight, Length, Diagonal, Height, Width => train feature
# print(pd.unique(fish['Species']))
fish_input=fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target=fish['Species'].to_numpy()

# print(fish_input[:5])
# print(fish_target[:5])
train_input,test_input,train_target,test_target= train_test_split(fish_input,fish_target,random_state=42)
# 표준점수로 변환
ss= StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input) 
test_scaled = ss.transform(test_input)
print(train_input[:5])
print(train_scaled[:5])
# print(test_scaled[:5])

knc= KNeighborsClassifier(n_neighbors=3) #하이퍼 파라메타
knc.fit(train_scaled,train_target)
predictvalue=knc.predict(test_scaled[:5])
print('훈련데이터 점수',knc.score(train_scaled,train_target))
print('테스트데이터 점수',knc.score(test_scaled,test_target))
print('predictvalue= ',predictvalue)

bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

print(bream_smelt_indexes)
print(train_bream_smelt[:5])
print(train_bream_smelt.shape)
print(target_bream_smelt[:5])
print(target_bream_smelt.shape)