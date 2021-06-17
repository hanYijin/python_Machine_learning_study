from flask import Flask,render_template, request
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/imgprint",methods=["POST"])
def imgprint():
    file = request.files['img_file']
    filename = f"static/{file.filename}"
    file.save(filename)

    img= cv2.imread(filename)
    img[100:200, 100:200] =[0,0,0]
    img[400:500, 400:500]=[255,255,255]
    ar= img[50:100, 50:100]
    img[0:50, 0:50]= ar;
    chfile= f"static/change{file.filename}"
    cv2.imwrite(chfile,img)
# 이미지 사이즈 확대
    img1=cv2.imread(filename)
    # 1.3배로 확대
    expand=cv2.resize(img1,None,fx=1.3,fy=1.3, interpolation=cv2.INTER_CUBIC)
    #파일명
    exfile=f"static/ex{file.filename}"
    #파일 저장
    cv2.imwrite(exfile,expand)
#이미지 사이즈 축소
    img1= cv2.imread(filename)
    shri= cv2.resize(img1,None,fx=0.3, fy=0.3,interpolation=cv2.INTER_AREA)
    shfile = f"static/sh{file.filename}"
    cv2.imwrite(shfile, shri)
# 이미지 축 기준으로 이동
    img1= cv2.imread(filename)
    m= np.float32([[1, 0 ,50, ],[0, 1, 100]])
    mimg= cv2.warpAffine(img1, m, (300,300))
    mfile=f"static/im{file.filename}"
    cv2.imwrite(mfile,mimg)

#이미지 회전
    img1= cv2.imread(filename)
    rot= cv2.getRotationMatrix2D((150,150),90,0.5)
    animg= cv2.warpAffine(img1,rot,(300,300))
    anfile = f"static/an{file.filename}"
    cv2.imwrite(anfile,animg)
    return  render_template("print.html",orifile=filename, chfile=chfile, exfile=exfile,shfile=shfile,\
                            mfile=mfile, anfile=anfile)

app.run(host="localhost", port=5000);
