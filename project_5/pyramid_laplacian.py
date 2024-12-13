import cv2
import numpy as np

img = cv2.imread("../img/taekwonv1.jpg")

# 가우시안 이미지 파라미드 축소
smaller = cv2.pyrDown(img) # img * 1/4
# 가우시안 이미지 파라미드 확대 # img * 4
bigger = cv2.pyrUp(smaller)

# 원본에서 확대한 영상 뺴기
laplacian = cv2.subtract(img, bigger)
# 확대한 영상에 라플라시안 영상 더해서 복원
restored = bigger + laplacian

#결과 출력 (원본영상, 라플라시안, 확댕 영상 복원 영상)
merged = np.hstack((img, laplacian, bigger, restored))
cv2.imshow('Laplacian Pyramid', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()