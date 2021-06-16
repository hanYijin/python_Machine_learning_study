import numpy as np
import cv2
from cv2 import IMREAD_COLOR, IMREAD_GRAYSCALE, IMREAD_UNCHANGED
import time
image= cv2.imread('static/test.jpg')
start= time.time()
for i in range(0,100):
    for j in range(0,100):
        image[i,j]=[255,255,255]
print("--- %s seconds---" %(time.time()-start))

start=time.time()
image[0:100,0:100]=[0,0,0]
print("--- %s seconds---" %(time.time()-start))

cv2.imshow("image",image)
cv2.waitKey(0)