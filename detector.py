import numpy as np
import dlib
import cv2
import face_recognition
import os
import subprocess
import time

# initialize dlib's face detector, user img, ...
detector = dlib.get_frontal_face_detector()
user_images = []
user_encodings = []
out = None
unknown_ID = 0
lasttime = 0

def initial():
      global user_images
      global user_encodings
      # read user list from file
      i = 0
      while True:
            try:
                  user_images.append(face_recognition.load_image_file("user" + str(i) + ".jpg"))
                  user_encodings.append(face_recognition.face_encodings(user_images[i])[0])
                  i += 1
            except:
                  break
      recordstart()
      print("[INFO] User images initialized!")

def detect(frame):
      global lasttime
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      # detect faces in the grayscale frame
      rects = detector(gray, 0)
      flag = False
      # if there is face, detect if it is unknown
      if len(rects) > 0:
            cv2.imwrite("unknown.jpg", frame)
            unknown_image = face_recognition.load_image_file("unknown.jpg")          
            try:
                  unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                  results = face_recognition.compare_faces(user_encodings, unknown_encoding, tolerance = 0.5)
                  unknown = True
                  for i in range(len(results)):
                        if results[i] == True:
                              unknown = False
                              break
                  # if unknown, record it
                  if unknown:
                        print("unknown detected")
                        if time.time() - lasttime >= 5:
                              subprocess.run(["python3", "bot.py"])
                              lasttime = time.time()
                        out.write(frame)
                        flag = True
                  else:
                        os.remove("unknown.jpg")            
            except IndexError:
                  pass    
      elif flag:
            release()

def recordstart():
      global out
      # Define the codec and create VideoWriter object
      fourcc = cv2.VideoWriter_fourcc(*'mp4v')
      out = cv2.VideoWriter("unknown" + str(unknown_ID) + ".mp4",fourcc, 20.0, (640, 480))

def release(out):
      global unknown_ID
      unknown_ID += 1
      out.release()
      recordstart()