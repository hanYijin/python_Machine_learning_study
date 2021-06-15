import numpy as np
import cv2
from cv2 import IMREAD_COLOR, IMREAD_GRAYSCALE, IMREAD_UNCHANGED

img_color=cv2.imread("static/test.jpg",IMREAD_COLOR)
img_gray=cv2.imread("static/test.jpg",IMREAD_GRAYSCALE)
img_unch=cv2.imread("static/test.jpg",IMREAD_UNCHANGED)

cv2.imshow("img_color",img_color)
cv2.imshow("img_gray",img_gray)
cv2.imshow("img",img_unch)
cv2.waitKey(0)
