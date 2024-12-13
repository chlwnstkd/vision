import cv2

# 이미지 읽기
image = cv2.imread("../img/my_face.jpg", cv2.IMREAD_GRAYSCALE)

# 이미지 반전
inverted_image = cv2.bitwise_not(image)

# 가우시안 블러 적용
# 스케치 구현할때 블러 크기가 클 수로 좀 더 스케치 느낌남
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# 텀블러 이미지를 다시 반전
inverted_blurred = cv2.bitwise_not(blurred)

# 원본 이미지와 반전된 블러 이미지를 나눠서 스케치 효과 적용
sketch = cv2.divide(image, inverted_blurred, scale=256.0)

cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()