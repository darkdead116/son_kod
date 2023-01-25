import cv2
import numpy as np 
from matplotlib import pyplot as plt


siyah = 0
beyaz= 255
img = cv2.imread("img.bmp")



resim = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

num_labels, labels = cv2.connectedComponents(resim)


label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_)

labeled_img[label_hue==0] = 0


plt.imshow(cv2.cvtColor(img, cvt2.COLOR_GRAY2RGB))
plt.axis("off")
plt.title("Orginal Image")
plt.show()

plt.imshow(cv2.cvtColor(labeled_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("Image after Component Labeling")
plt.show()



cv2.namedWindow("son_hal", cv2.WINDOW_NORMAL)

cv2.imshow("son_hal", output)

cv2.waitKey(0)
