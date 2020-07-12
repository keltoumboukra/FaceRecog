# Face recognication on live image

import cv2
import dlib

# get detector
detector = dlib.get_frontal_face_detector()
# get trained prdictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# live reading
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # convert image into grayscale
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    # use detector and draw dots
    faces = detector(gray)
    for face in faces:
        x1 = face.left()  # left point
        y1 = face.top()  # top point
        x2 = face.right()  # right point
        y2 = face.bottom()  # bottom point
        # look for the landmarks
        landmarks = predictor(image=gray, box=face)
        # loop over all the points (68)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            # add dot
            cv2.circle(img=frame, center=(x, y), radius=2, color=(255, 55, 255), thickness=-1)
    # show the image
    cv2.imshow(winname="Face", mat=frame)
    # to stop, preess escape key
    if cv2.waitKey(delay=1) == 27:
        break

# release video and close window
cap.release()
cv2.destroyAllWindows()
