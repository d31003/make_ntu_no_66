import numpy as np
import argparse
import dlib
import cv2
import face_recognition
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user_ID", required=True,
                help="update userX.jpg via ID=X")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)

# initial current user
user_ID = str(args["user_ID"])
user_image = None
user_encoding = None
filename = "user" + user_ID + ".jpg"

while True:
   ret, frame = cap.read()      
   # show the frame
   cv2.imshow("Frame", frame)
   key = cv2.waitKey(1) & 0xFF
   
   # if the 'p' key was pressed, then try to initialize
   if key == ord("p"):
      cv2.imwrite(filename, frame)
      # if the recorded image is OK to be recognized, complete initial
      try:
         user_image = face_recognition.load_image_file(filename)
         user_encoding = face_recognition.face_encodings(user_image)[0]
         print("[INFO] Initial complete!")
         break
      # else try again
      except IndexError:
         print("[INFO] Initial failed! Try Again!")
         os.remove(filename)
         pass         

   # if 'q' is pressed, end initial
   if key == ord("q"):
      cv2.destroyAllWindows()
      break
 
# cleanup
exit()
