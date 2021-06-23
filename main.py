import cv2
import time
webcam, laptop_cam = 1, 0
cap = cv2.VideoCapture(webcam)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
while True:
    frame = cap.read()[1]
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for face_x, face_y, face_w, face_h in face:
        cv2.rectangle(frame, (face_x, face_y), ((face_x+face_w), (face_y+face_h)), (255, 255, 0)[::-1], 2)
        face_roi = frame[face_y:(face_y+face_h), face_x:(face_x+face_w)]
        gray_roi = gray[face_y:(face_y+face_h), face_x:(face_x+face_w)]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        for smile_x, smile_y, smile_w, smile_h in smile:
            cv2.rectangle(face_roi, (smile_x, smile_y), ((smile_x+smile_w), (smile_y+smile_h)), (255, 0, 0)[::-1], 2)
            time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f"images/selfie-{time_stamp}.png"
            cv2.imwrite(file_name, original_frame)
    cv2.imshow('cam star', frame)
    if cv2.waitKey(10) == ord('q'):
        break
