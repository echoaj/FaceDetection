import face_recognition
import cv2
import time

image = face_recognition.load_image_file("group.jpg")
face_locations = face_recognition.face_locations(image)

print(f"There are {len(face_locations)} people in image.") #print("Number of people in image:", len(face_locations))
