import numpy as np
import cv2

#cap = cv2.VideoCapture("./../../../media/open-cv/Plainsight_Axis Vehicle video.mkv")
#cap = cv2.VideoCapture("./../../../media/open-cv/plainsight-vehicle-video.m4v")
cap = cv2.VideoCapture("./../Vehicle-Detection-Project/Resources/video2.mp4")

#cap = cv2.VideoCapture("./../../../media/open-cv/cars.mp4")
##face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Use CascadeClassifier for car detection
#car_cascade_src = './haarcascade_cars.xml'
#car_cascade_src = './cars.xml'
car_cascade_src = './cars-1.xml'

car_cascade = cv2.CascadeClassifier(car_cascade_src)
#cars = car_cascade.detectMultiScale(closing, 1.1, 1)


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ##  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()