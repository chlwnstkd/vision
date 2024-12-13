import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

age_net = cv2.dnn.readNetFromCaffe("../model/deploy_age.prototxt", "../model/age_net.caffemodel")

gender_net = cv2.dnn.readNetFromCaffe("../model/deploy_gender.prototxt", "../model/gender_net.caffemodel")

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

age_list = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]

gender_list = ["Male", "Female"]

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.equalizeHist(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:

        face_img = frame[y:y+h, x:x+w]

        blob = cv2.dnn.blobFromImage(face_img, scalefactor=1.0, size=(227, 227), mean=MODEL_MEAN_VALUES, swapRB=False)

        gender_net.setInput(blob)

        gender = gender_list[gender_net.forward().argmas()]

        age_net.setInput(blob)

        age = age_list[age_net.forward().argmax()]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(frame, f"{gender}, {age}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("Webcam - Gender and Age Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()