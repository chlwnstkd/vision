import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

age_net = cv2.dnn.readNetFromCaffe("../model/deploy_age.prototxt", "../model/age_net.caffemodel")

gender_net = cv2.dnn.readNetFromCaffe("../model/deploy_gender.prototxt", "../model/gender_net.caffemodel")

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

age_list = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]

gender_list = ["Male", "Female"]

image = cv2.imread("../img/face4.png")

if image is None:
    raise Exception("이미지를 불러올 수 없습니다.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(100, 100))

for (x, y, w, h) in faces:

    face_img = image[y:y+h, x:x+w]

    blob = cv2.dnn.blobFromImage(face_img, scalefactor=1.0, size=(227, 227), mean=MODEL_MEAN_VALUES, swapRB=False)

    gender_net.setInput(blob)

    gender_preds = gender_net.forward()

    gender = gender_preds.argmax()

    age_net.setInput(blob)

    age_preds = age_net.forward()

    age = age_preds.argmax()

    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    result_text = f"{gender_list[gender]}, {age_list[age]}"
    cv2.putText(image, result_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    # 콘솔에 텍스트 출력
    print(result_text)

cv2.imshow("Gender and Age Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()