import cv2
import numpy as np

def chage_colors():
    print("바뀌고 있음")
    pass
img= np.zeros((600,300,3),dtype=np.uint8)
cv2.nameWindow("Image")

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

