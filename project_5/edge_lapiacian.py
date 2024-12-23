import cv2
import numpy as np

img = cv2.imread("../img/sudoku.jpg")

# 라플라시안 필터 적용
edge = cv2.Laplacian(img, -1)

merged = np.hstack((img, edge))
cv2.imshow('Laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()