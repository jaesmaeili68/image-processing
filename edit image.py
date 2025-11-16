import cv2
import numpy as np

img = cv2.imread('E:\\Python Tutorial\\image processing\\Taylor-Cone.jpg')
resized = cv2.resize(img, (400, 400))
part1 = resized[100:200, 100:200]

resized[300:400, 300:400] = part1
cv2.imshow('image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()



