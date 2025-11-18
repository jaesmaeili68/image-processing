import cv2
import numpy as np

img = cv2.imread('E:\\Python Tutorial\\image processing\\text.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 8, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 2)

cv2.imshow('th', th)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()