import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('E:\\Python Tutorial\\image processing\\Taylor-Cone.jpg', cv2.IMREAD_GRAYSCALE)
resized = cv2.resize(img, (300, 300))
cv2.imshow('resized image', resized)
plt.imshow(resized, cmap='gray', interpolation='bicubic')
plt.plot([100, 100], [100, 300], 'b', linewidth=5)
plt.show()

cv2.imwrite('E:\\Python Tutorial\\image processing\\imgout.jpg', resized)
print ("the new image saved")