
import cv2
import numpy as np 
from matplotlib import pyplot as plt


resim = cv2.imread("img.bmp")

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

print(resim.shape)

detected_circles = cv2.HoughCircles(gray, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 70,
               param2 = 90, minRadius = 50, maxRadius = 350)





detected_circles = np.uint16(np.around(detected_circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(resim, (x, y), r, (0, 255, 0), 2)
    cv2.circle(resim, (x, y), 2, (255, 0, 0), 2)
    

print(r)
    
cv2.namedWindow("son_hal", cv2.WINDOW_NORMAL)

cv2.imshow("son_hal", resim)


cv2.waitKey(0)