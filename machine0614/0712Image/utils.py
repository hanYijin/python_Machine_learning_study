'''
가지고온 이미지들을 cv2
cv2.imread 하게 되면 numpy배열로
numpy배열 알고리즘으로 이미지 분석

cv2 (r,g,b)
'''
import cv2
GREEN=0
BULE=1
RED=2

def getcolors(img,color):
    other_1=(color + 1) % 3
    other_2=(color+2) % 3
    #불리언 인덱싱
    indexes = img [:,:,other_1]==255
    img[indexes]=[0,0,0]
    # cv2.imshow('image', img)
    # cv2.waitkey(0)
    indexes= img[:,:,other_2]==255
    img[indexes]=[0,0,0]
    # cv2.imshow('image', img)
    # cv2.waitkey(0)
    indexes= img[:,:,color]<170
    img[indexes]=[0,0,0]
    # cv2.imshow('image', img)
    # cv2.waitkey(0)
    indexes=img[:,:,color] != 0
    img[indexes]=[255,255,255]
    # cv2.imshow('image', img)
    # cv2.waitkey(0)
    return img