import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
tomato=pd.read_csv('tomato.csv')
# print(tomato.describe())
data=tomato[['생장길이', '화방높이', '줄기굵기', '잎길이(엽장)', '착과군', '개화군']].to_numpy()
target = tomato['열매수'].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2,random_state=42)
print(train_input.shape,test_input.shape)

ss= StandardScaler()
ss.fit(train_input)
train_scaled=ss.transform(train_input)
test_scaled=ss.transform(test_input)

lr=LogisticRegression()
lr.fit(train_input,train_target)
# print(lr.score(train_scaled,train_target))
print(lr.score(test_scaled,test_target))