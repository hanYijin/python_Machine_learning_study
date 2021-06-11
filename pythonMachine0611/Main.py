# flask 웹 모듈 라이브러리
# sklearn 알고리즘...라이브러리
# matplib 그래프 그려주는 라이브러리
# api

from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

@app.route("/")
def home():
    wlength = request.args.get("length",default=30, type= float) # 입력값 없을떄 기본 값 30 , 자료형 타입 설정
    wweight = request.args.get("weight", default=600, type=float)# 입력값 없을떄 기본 값 600, 타입 설정 안할시 문자열로 받음
    # 도미 데이터
    bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0,
                    33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5,
                    39.5, 41.0, 41.0]
    bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0,
                    600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0,
                    850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
    # 빙어 데이터
    smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
    smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

    plt.scatter(bream_length, bream_weight, marker='o') # 도미데이터 그리기
    plt.scatter(smelt_length, smelt_weight, marker='*') # 빙어데이터 그리기

    plt.scatter(wlength,wweight, marker='^') # x,y (30,600) 좌표에 세모 마커 추가

    plt.xlabel('length')
    plt.ylabel('weight')
    #plt.show()
    brimg= f"static/brimg.png"
    plt.savefig(brimg)
    plt.close() #리소스 닫기

    length = bream_length+ smelt_length  # x 배열 합치기
    weight = bream_weight + smelt_weight # y 배열 합치기

    #2차원 배열
    fish_data =[[l,w] for l,w in zip(length,weight)]
    print(fish_data)

    # 도미 데이터 : 1 양성 데이터
    # 빙어 데이터: 0 음성 데이터
    fish_target =[1]*35 +[0]*14
    print(fish_target)

#k-최근접 이웃 알고리즘
    knc= KNeighborsClassifier(n_neighbors=20)
    knc.fit(fish_data,fish_target) #데이터 만든 것 넣는 함수
    svalue=knc.score(fish_data,fish_target) # 이 데이터를 넣을떄 알고리즘 확률
    tvalue=knc.predict([[wlength,wweight]]) # 데이터를 넣을때 1, 0 인지 판단하는 함수

    print('svalue',svalue)
    print('tvalue', tvalue)
    #좌표 30,600의 데이터가 도미인지 빙어인지 확인
    prevalue="도미"
    if tvalue == 1:
        prevalue="도미"
    else:
        prevalue="빙어"

    return render_template("index.html",brimg=brimg,prevalue=prevalue)

# 도미 데이터와 빙어데이터가 나열
app.run(host="localhost", port=5000)