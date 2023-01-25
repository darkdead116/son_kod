
import cv2
import numpy as np 
from matplotlib import pyplot as plt


resim = cv2.imread("img.bmp")

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

print(resim.shape)

ROI= np.array([[(1000,228),(1000,228),(232,850),(232,850)]], dtype= np.int32)

blank= np.zeros_like(gray)

region_of_interest= cv2.fillPoly(blank, ROI,255)

region_of_interest_image= cv2.bitwise_and(gray, region_of_interest)


se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))

mask = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, se1)

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)



mask = np.dstack([mask, mask, mask]) / 255
out = resim * mask


cv2.namedWindow("son_hal", cv2.WINDOW_NORMAL)

cv2.imshow("son_hal", out)


cv2.waitKey(0)