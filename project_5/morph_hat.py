import cv2
import numpy as np

img = cv2.imread("../img/moon_gray.jpg")

# 구조화 요소 커널, 사각형(9*9) 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))

# 탑햇 연산 적용
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
# 블핵햇 연산 적용
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)

merged3 = np.hstack((img, tophat, blackhat))
cv2.imshow('tophat blackhat', merged3)
cv2.waitKey(0)
cv2.destroyAllWindows()