import cv2
import numpy as np

img = cv2.imread('E:\Python Tutorial\image processing\Taylor-Cone.jpg')
resized = cv2.resize(img, (200, 200))

laplacian = cv2.Laplacian(resized, cv2.CV_8U)
sobelx = cv2.Sobel(resized, cv2.CV_8U, 1, 0, ksize=5)
sobely = cv2.Sobel(resized, cv2.CV_8U, 0, 1, ksize=5)
# The output type of the image (8-bit unsigned).
# That is, the intensity of the pixels will be between 0 and 255.
canny = cv2.Canny(resized, 50, 150)


cv2.imshow('original', resized)
cv2.imshow('laplacian', laplacian)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('Canny', canny)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
