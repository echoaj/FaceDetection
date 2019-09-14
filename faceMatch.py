import face_recognition

image_of_obama = face_recognition.load_image_file("Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]
print(obama_face_encoding)

unknown_image= face_recognition.load_image_file("oprah.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]  #important note
#In the case of oprahObama photo, it will only match 1 of the if [0] because there is two people
#in the photo so to match obama change it to [1]


#compare faces
results = face_recognition.compare_faces([obama_face_encoding], unknown_face_encoding)

if results[0]:
    print("This is Obama")
else:
    print("This is not Obama")