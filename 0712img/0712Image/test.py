import utils
import cv2

img = cv2.imread('images/d2.png', cv2.IMREAD_COLOR)
utils.extract_chars(img)
# green_img = utils.getcolors(img.copy(), utils.GREEN)
# cv2.imshow('image', green_img)
# cv2.waitKey(0)
#
# blue_img = utils.getcolors(img.copy(), utils.BULE)
# cv2.imshow('image', blue_img)
# cv2.waitKey(0)
# #
# red_img = utils.getcolors(img.copy(), utils.RED)
# cv2.imshow('image', red_img)
# cv2.waitKey(0)


