import cv2
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=['post'])
def upload():
    image=request.files['img_file']
    imageName=f"static/{image.filename}"
    image.save(imageName)

    chimg= cv2.imread(imageName)
    chimg[100:200,100:200]=[0,0,0]
    chimg[300:400,300:400]=[255,255,255]
    ar=chimg[50:100,50:100]
    chimg[0:50,0:50]=ar;
    chfile= f"static/ch{imageName}"
    cv2.imwrite(chfile,chimg)
    #이미지 확대
    img=cv2.imread(imageName)
    #사용할 보간법(interpolation methods) 지정
    #이미지 확대할때는 cv2.INTER_CUBIC 또는 cv2.INTER_LINEAR을 권장
    # cv2.INTER_CUBIC는 좀더 선면한 이미지를 얻을 수 있다. 처리속도는 느림
    bigimg=cv2.resize(img,None,fx=2.0,fy=2.0,interpolation=cv2.INTER_CUBIC)
    bigfile=f"static/big{imageName}"
    cv2.imwrite(bigfile,bigimg)
    #이미지 축소
    smallimag=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    smallfile=f"static/small{imageName}"
    cv2.imwrite(smallfile,smallimag)

    #이미지 회전
    height,width= img.shape[:2]
    rot=cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
    turnimg=cv2.warpAffine(img,rot,(width,height))
    turnfile=f"static/turn{imageName}"
    cv2.imwrite(turnfile,)


    #cv2.INTER_AREA는 이미지 축소할때 권장
    #bigimg2 = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_AREA)

    return render_template("print.html",image=image.filename,chimgfile= chimgfile,bigimgName=bigimgName,smallimag=smallimag.filname)

app.run(host="localhost", port=5000);
# img = cv2.imread('static/test.jpg')
# #픽셀 수 및 이미지 크기 확인
# print(img.shape) #(554, 749, 3)
# print(img.size) #1244838
#
# #이미지 numpy 객첵의 특정 픽셀을 가리킴
# px= img[100,100]
# print(px) #[234 74 64] B, G, R 순서로 출력
# print(px[2]) # 64 R 값만 출력