import numpy
import face_recognition
import cv2
from time import sleep
import random

#print(cv2.__file__)
face_cascade = cv2.CascadeClassifier('/Users/alexjoslin/venv/selfFacialRecognition/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)   #turns on camara

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      #We are converting the color of the frame to gray
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      #THANOS

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)  #array of subarrays with 4 elements
    for(x,y,w,h) in faces:

        # uncomment this to take a picture of yourself
        # img_gray =gray[y:y+h, x:x+w] #[cord1+height, cord2-height]
        # img_color = frame[y:y+h, x:x+w]
        # img_name = "myself.png"
        # cv2.imwrite(img_name, img_gray)

        color = (0, int(w-255), int(350-w))  # BGR of rectangle
        stroke = 5  # width of square
        end_coord_x = x + w
        end_coord_y = y + h
        cv2.rectangle(frame, (x,y), (end_coord_x, end_coord_y), color, stroke)


    cv2.imshow('Frame', frame)                                      #makes video appear with title frame
    if cv2.waitKey(20) & 0xFF == ord('q'):                          #press q to quit
        break

cap.release()
cv2.destroyAllWindows()















# MAKE IT SO IT CAN DETECT YOU
# me_image = face_recognition.load_image_file("me.png")
# me_face_encoding = face_recognition.face_encodings(me_image)[0]
#
# video_image = face_recognition.load_image_file("my_image.png")
# my_image_face_encoding = face_recognition.face_encodings(video_image)
#
# for i in my_image_face_encoding:
#     results = face_recognition.compare_faces([me_face_encoding], i)
#     if results[0]:
#         print("Alex detected")
#     else:
#         print("Not Here")