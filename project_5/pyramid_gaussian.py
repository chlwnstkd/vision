import cv2
import numpy as np

img = cv2.imread("../img/girl.png")

# 가우시안 이미지 파라미드 축소
smaller = cv2.pyrDown(img) # img * 1/4
# 가우시안 이미지 파라미드 확대 # img * 4
bigger = cv2.pyrUp(img)

cv2.imshow('img', img)
cv2.imshow('smaller', smaller)
cv2.imshow('bigger', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()