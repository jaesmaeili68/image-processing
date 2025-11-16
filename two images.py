import cv2
import numpy as np

img1 = cv2.imread('E:\\Python Tutorial\\image processing\\Taylor-Cone.jpg')
img2 = cv2.imread('E:\\Python Tutorial\\image processing\\green cone.jpg')
img1R = cv2.resize(img1, (300, 300))
img2R = cv2.resize(img2, (300, 300))

# ✅ 1. To put one image on another one
blend = img1R + img2R
cv2.imshow('add', blend)

# ✅ 2. Putting two images together
combined = np.hstack((img1R, img2R))
cv2.imshow('combined', combined)

# ✅ 3. Copying part of one image to another
part = img2R[50:100, 50:100]
img1R[50:100, 50:100] = part
cv2.imshow('added', img1R)

# ✅ 4. blend two images
blend_2 = cv2.addWeighted(img1R, 0.2, img2R, 0.3, 0)
cv2.imshow('blend2', blend_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
