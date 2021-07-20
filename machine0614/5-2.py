import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate #교차 검증
from scipy.stats import uniform, randint #랜덤 서치
from sklearn.model_selection import RandomizedSearchCV #랜덤 서치
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
#교차검증
'''
    학습:테스트 =80:20
    교차 검증 학습 80 => 60:20
'''
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)
#교차 검증을 위한 데이터 분리

sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

# print(sub_input.shape, val_input.shape)

dt=DecisionTreeClassifier(random_state=42)
dt.fit(sub_input,sub_target)

print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

cores= cross_validate(dt,train_input,train_target)
print(cores)
#'fit_time','score_time','test_score'
print('테스트 검증 값의 평균:',np.mean(cores['test_score']))

from sklearn.model_selection import StratifiedKFold
cores= cross_validate(dt,train_input,train_target,cv=StratifiedKFold())
print(cores)
print('테스트 검증 값의 평균:',np.mean(cores['test_score']))

splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))


#하이퍼파라미터 튜닝
from sklearn.model_selection import GridSearchCV

params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1) # n_jobs=-1: cpu병렬처리
gs.fit(train_input, train_target)
print(gs)

dt=gs.best_estimator_
print(dt.score(train_input, train_target))

print(gs.best_params_)

print(gs.cv_results_['mean_test_score'])
best_index = np.argmax(gs.cv_results_['mean_test_score'])
print(gs.cv_results_['params'][best_index])

params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
          'max_depth': range(5, 20, 1),
          'min_samples_split': range(2, 100, 10)
          }
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)

rgen = randint(0, 10)
rgen.rvs(10)
np.unique(rgen.rvs(1000), return_counts=True)
ugen = uniform(0, 1)
ugen.rvs(10)

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25),
          }

gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params,
                        n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)
print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))

dt = gs.best_estimator_

print(dt.score(test_input, test_target))
'''
    로지스틱리그레이션
    와인.. 분류: 77점 86점
    
    결정트리분류: 96점 86점
    
    교차검증 corssvalidate 
    결정트리는 하이퍼파라미터로 max_depth,impurity_decrease 사용된다
    GridSearchCV, RandomizedSearchCV로 하이퍼파라미터 튜닝
'''