import cv2

import utils
import os

imgs = cv2.imread('images/d0.png', cv2.IMREAD_COLOR)
chars=utils.extract_chars(imgs)

for char in chars:
    cv2.imshow('char[1]',char[1])
    input = cv2.waitKey(0)
    resized= utils.resized20(char[1])
    print('input',input)
    print('input -48',input-48)
    # +: a , -:b , *: c
    if input >= 48 and input <= 57:
        name = str(input - 48)
        # print('len(next(os.walk(./training_data/+ name + /))[2]')
        # print( len(next(os.walk('./training_data/' + name + '/'))[2]))
        if not os.path.isdir('./training_data'):
            os.makedirs('./training_data')
        if not os.path.isdir('./training_data/' + name):
            os.makedirs('./training_data/' + name)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + str(input - 48) + '/' +
                    str(file_count + 1) + '.png', resized)
    elif input == ord('a') or input == ord('b') or input == ord('c'):
        #파이썬 내장함수 ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.
        name = str(input - ord('a') + 10) #>>> ord('a'): 97
        if not os.path.isdir('./training_data'):
            os.makedirs('./training_data')
        if not os.path.isdir('./training_data/' + name):
            os.makedirs('./training_data/' + name)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + name + '/' +
                    str(file_count + 1) + '.png', resized)