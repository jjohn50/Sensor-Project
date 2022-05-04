"""
Limitation of face recognition:
    - if there is a face covering or somethign obstructing the face it will not detect a faced
    - takes 10-15 sec to process image and provide output
    
"""

import face_recognition

image = face_recognition.load_image_file("Cosplay.jpg")
face_location = face_recognition.face_locations(image)
#face_landmarks_list = face_recognition.face_landmarks(image)

count = 0
for element in face_location:
    count = count + 1
    
if count > 0:
    print("There is a faceeeee !!!!!")
    
#print(face_landmarks_list)
print(face_location)
