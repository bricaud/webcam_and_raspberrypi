import cv2
import numpy as np
import os
import sys
import detection




# initializing face recognition methods
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(detection.model_file)
person_id2name = detection.read_person_names(detection.person_names_file)
confidence_threshold = 20

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) # mirror
    faces,gray = detection.get_faces(img, face_detector)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        person_id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if ((100 - confidence) > confidence_threshold):
            person_name = person_id2name[str(person_id)]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            person_name = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(person_name), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()