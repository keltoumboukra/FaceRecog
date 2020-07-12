# Face detection on static image

import cv2
import dlib
import numpy as np

# get detector
detector = dlib.get_frontal_face_detector()
# get trained prdictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# read the image
img = cv2.imread("zidane.jpg")
# convert image into grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# use detector and draw dots
faces = detector(gray)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    # look for the landmarks
    landmarks = predictor(image=gray, box=face)
    # Loop through all the points
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        # add dots on landmarks
        cv2.circle(img=img, center=(x, y), radius=2, color=(255, 55, 255), thickness=-1)
# open image in window
cv2.imshow(winname="Face", mat=img)
# close window after pressing key
cv2.waitKey(delay=0)
cv2.destroyAllWindows()