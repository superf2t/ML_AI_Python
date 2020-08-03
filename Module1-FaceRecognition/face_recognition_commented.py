# Face Recognition

import numpy as np
import cv2

#import cv

face_cascade = cv2.CascadeClassifier("/Users/makanfofana/Downloads/Computer_Vision_A_Z_Template_Folder/Module1-FaceRecognition/haarcascade_frontalface_default.xml") 
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#cv2.CascadeClassifier('/Users/makanfofana/Downloads/Computer_Vision_A_Z_Template_Folder/Module1-FaceRecognition/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/Users/makanfofana/Downloads/Computer_Vision_A_Z_Template_Folder/Module1-FaceRecognition/haarcascade_eye.xml')

def detect(gray, frame): # We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.
        roi_gray = gray[y:y+h, x:x+w] # We get the region of interest in the black and white image.
        roi_color = frame[y:y+h, x:x+w] # We get the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # We apply the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) # We paint a rectangle around the eyes, but inside the referential of the face.
    return frame # We return the image with the detector rectangles.

video_capture = cv2.VideoCapture(-1) # We turn the webcam on.


    
while True: # We repeat infinitely (until break):
    _, frame = video_capture.read() # We get the last frame.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
    canvas = detect(gray, frame) # We get the output of our detect function.
    cv2.imshow('Video', canvas) # We display the outputs.
    if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
        break # We stop the loop.

video_capture.release() # We turn the webcam off.
cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.















#while(video_capture.isOpened()):  # check !
#    # capture frame-by-frame
#    ret, frame = video_capture.read()
#
#    if ret: # check ! (some webcam's need a "warmup")
#        # our operation on frame come here
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#        # Display the resulting frame
#        cv2.imshow('frame', gray)
#
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break