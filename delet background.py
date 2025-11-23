import cv2
import numpy as np

video_path = r"E:\Python Tutorial\image processing\video1.MP4"
cap = cv2.VideoCapture(video_path) 
fg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    fmask = fg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fmask)

    k = cv2.waitKey(27) & 0xFF
    if (k==27):
      break

cv2.destroyAllWindows()
cap.release()