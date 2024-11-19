import cv2
import numpy as np

# 이미지를 읽어서 바이너리 스케일로 변환
img = cv2.imread('../img/full_body.jpg', cv2.IMREAD_GRAYSCALE)
_, biimg = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 거리 변환
dst = cv2.distanceTransform(biimg, cv2.DIST_L2, 5)
# 거리 값을 0 ~ 255 범위로 정규화
dst = (dst/(dst.max()-dst.min()) * 255).astype(np.uint8)
# 거리 값에 스레시홀드로 완전한 뼈대 찾기
skeleton = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                 cv2.THRESH_BINARY, 7, -3)

# 결과 출력
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('skeleton', skeleton)
cv2.waitKey()
cv2.destroyAllWindows