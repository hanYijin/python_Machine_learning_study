
from flask import Flask, render_template,request
import cv2
#opencv-pythion
#numpy
#flask

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
'''
    templates 폴더에다가  html 파일들을 넣고 static 폴더에다가 image파일이나 js, css등을 넣으면 됨
'''
@app.route("/upload", methods=['post'])
def upload():
    image = request.files['file']
    image.save(f"static/{image.filename}")
    print(image.filename)

    npimage = cv2.imread(f"static/{image.filename}")
    #npimage[0:100, 0:100] = [0,0,0] #빨강,파랑,초록 모두 섞은 흰색
    roi = npimage[150:200, 200:350]
    npimage[0:150,0:150] =roi
    npimage[:,:,2]=0 # 색상 초록색으로 변경

    npimagename = f"static/np{image.filename}"

    #npimage.save(npimagename)
    cv2.imwrite(npimagename,npimage) #numpy 배열에 이미지화 저장
    return render_template("print.html", image=image.filename, npimage=npimagename)

app.run(host="localhost", port=5000);

#tomcat -> 9000
#index.jsp <a href="localhost:5000/index.html></a>

#python flask -> 5000