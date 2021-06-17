from flask import Flask, request, render_template
import numpy as np
import cv2

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addimg",methods=["post"])
def addimg():
    file1=request.files['file1']
    file2=request.files['file2']
    file1name=f"static/{file1.filename}"
    file2name=f"static/{file2.filename}"
    file1.save(file1name)
    file2.save(file2name)

    img1=cv2.imread(file1name)
    img2=cv2.imread(file2name)
    img3= cv2.add(img1,img2)

#    img4= np.add(img1+img2)
    addimg=f"static/addimg"
    #npaddimg=f"static/npaddimg"
    cv2.imwrite(addimg,img3)
    #cv2.imwrite(npaddimg,img4)
    return render_template("print1.html",cv2add=addimg)

app.run(host="localhost", port=5000, debug=True)