import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret,frame =cam.read()
    ret,frame =cam.read()
    if cv2.waitKey(10) == ord('t'):
        break

    cv2.imshow('kc emma', frame)
