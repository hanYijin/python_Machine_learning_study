import utils
import cv2

img=cv2.imread('images/d2.png',cv2.IMREAD_COLOR)
green_img=utils.getcolors(img.copy(),utils.GREEN)
cv2.imshow('image',green_img)
cv2.waitkey(0)

blue_img= utils.getcolors(img.copy(),utils.BULE)
cv2.imshow('image',blue_img)
cv2.waitkey(0)

red_img= utils.getcolors(img.copy(),utils.red)
cv2.imshow('image',red_img)
cv2.waitkey(0)

#utils.getchars()