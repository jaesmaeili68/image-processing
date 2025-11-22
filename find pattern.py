import cv2
import numpy as np

img = cv2.imread('E:\Python Tutorial\image processing\imageF.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



imgtemp = cv2.imread('E:\Python Tutorial\image processing\imageT.png', 0)
h, w = imgtemp.shape

res = cv2.matchTemplate(img1, imgtemp, cv2.TM_CCOEFF_NORMED)
threshhold = 0.8

loc = np.where(res >= threshhold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 1)

cv2.imshow('taylor coneT', img)
cv2.imshow('taylor cone', imgtemp)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
