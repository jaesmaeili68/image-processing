import cv2
import numpy as np
import matplotlib.pyplot as plt

imgtemp = cv2.imread('E:\Python Tutorial\image processing\Taylor-ConeT.jpg', 0)
img = cv2.imread('E:\Python Tutorial\image processing\Taylor-Cone1.jpg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(imgtemp, None)
kp2, des2 = orb.detectAndCompute(img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

img_out = cv2.drawMatches(imgtemp, kp1, img, kp2, matches[:100], None, flags=2)
plt.imshow(img_out)
plt.show()

