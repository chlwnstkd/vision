import cv2

img_file = '../img/girl.jpg'
save_file = './img/girl_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)  # 읽은 이미지를 화면에 표시
cv2.imwrite(save_file, img) # 파일로 저장, 포맷은 확장에 따름
cv2.waitKey()  # 키가 입력될 때 까지 대기
cv2.destroyAllWindows()  # 창 모두 닫기
