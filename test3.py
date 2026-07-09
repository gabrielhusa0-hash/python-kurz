import cv2
import numpy as np

faces_data = []
i = 0
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(grey, 1.3, 5)
    for (x,y,w, h) in faces:
        cro_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2. resize(crop_img, (50, 50))
        if len(faces_data) <= 100 and i  % 10 == 0:
            faces_data.append(resized_img)
        i += 1
    