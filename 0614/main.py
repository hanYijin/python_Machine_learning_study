#flask 웹
# sklearn 머신러닝 알고리즘
# matpalotlib 그래프

from flask import Flask, render_template
from alone21 import marketraintest

app= Flask(__name__)

#numpy as np
#np.arange(10) =>[0,1,2,3,4,5,6,7,8,9]
#np.random.seed(42) : 랜덤한 값이 똑같은 패턴으로 나오게

# np 문법
# slice, indicate
# [:35],  [1,3,5]

# KNeighborsClassifier
# fiter() 데이터 학습
# sorco

@app.route("/")
def index():
    marketraintest()
    return render_template("index.html")

app.run(host='localhost', port=5000)
