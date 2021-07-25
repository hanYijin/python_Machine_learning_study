import utils
import cv2

img = cv2.imread('images/d2.png', cv2.IMREAD_COLOR)
utils.extract_chars(img)
print(img.shape)
print(img.size)
print(img[10,32])


