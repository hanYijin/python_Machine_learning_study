#flask 웹
# sklearn 머신러닝 알고리즘
# matpalotlib 그래프

from flask import Flask, render_template
from alone21 import marketraintest
import numpy as np
import matplotlib.pyplot as plt
# app= Flask(__name__)

import cv2

img1 = cv2.imread("static/image_1.jpg",)
img2 = cv2.imread("static/image_2.png")

try:
    cv2.imshow("img1", img1)
    # a = input()
    cv2.waitKey(0)
except Exception as e:
    print(e)

img3= cv2.add(img1,img2)

cv2.imshow("img3",img3)
cv2.waitKey(100)
#
img4= np.add(img1,img2)
cv2.imshow("img4",img4)
cv2.waitKey(0)
cv2.imwrite("img3.png",img3)

#numpy as np
#np.arange(10) =>[0,1,2,3,4,5,6,7,8,9]
#np.random.seed(42) : 랜덤한 값이 똑같은 패턴으로 나오게

# np 문법
# slice, indicate
# [:35],  [1,3,5]

# KNeighborsClassifier
# fiter() 데이터 학습
# sorco

# @app.route("/")
# def index():
#     marketraintest()
#     return render_template("index.html")
#
# app.run(host='localhost', port=5000)
