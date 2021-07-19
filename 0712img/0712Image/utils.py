'''
    가지고온 이미지들을 cv2
    cv2.imread 하게되면..numpy 배열로....
    numpy 나온걸 이웃알고리즘....
    cv2.imread predict 하게되면... 어떤...
'''
import numpy as np

import cv2
GREEN = 0
BLUE = 1
RED = 2

def resized20(img):
    resized = cv2.resize(img,(20,20))
    return resized.reshape(-1,400).astype(np.float32)

def getcolors(img, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3
    # 불리언 인덱싱
    indexes = img[:, :, other_1] == 255
    img[indexes] = [0, 0, 0]
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    indexes = img[:, :, other_2] == 255
    img[indexes] = [0, 0, 0]
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    indexes = img[:, :, color] < 170
    img[indexes] = [0, 0, 0]
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    indexes = img[:, :, color] != 0
    img[indexes] = [255, 255, 255]
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    return img

def extract_chars(img):
    chars = []
    colors = [BLUE,GREEN,RED]
    for color in colors:
        imgs = getcolors(img.copy(),color)
        gray_imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2GRAY)   #흑백처리
        ret, thre_imgs = cv2.threshold(gray_imgs,127,255,cv2.THRESH_BINARY) #쓰레스홀드.. 한계점.. 127이상 255 127미만 0처리
        # 외곽선을 찾아라
        contours, _ = cv2.findContours(thre_imgs,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            #cv2.drawContours(gray_imgs, contour,0,(0,0,255),2)
            # cv2.imshow('text',gray_imgs)
            # cv2.waitKey(0)
            area = cv2.contourArea(contour)
            #cv2.contourArea() 외곽선이 감싸는 영역의 면적을 반환합니다.
            # print('area',area)
            if area > 50:
                x,y,width,height = cv2.boundingRect(contour)
                roi = gray_imgs[y:y+height, x:x+width]
                chars.append((x,roi))
                # cv2.imshow('roi',roi)
                # cv2.waitKey(0)

    chars = sorted(chars, key = lambda char:char[0])
    return chars















