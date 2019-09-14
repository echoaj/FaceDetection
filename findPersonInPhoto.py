import face_recognition

image_of_obama = face_recognition.load_image_file("Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]

unknown_image= face_recognition.load_image_file("obamaGroup.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)

#compare faces
for i in unknown_face_encoding:
    results = face_recognition.compare_faces([obama_face_encoding], i)
    if results[0]:
        print("Obama was found in image")

