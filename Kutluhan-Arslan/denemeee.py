import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)
im = cv2.imread("img.bmp", 0)  # dosyayi oku
plt.subplot(2, 2, 1)
plt.imshow(im, cmap="gray")

# inverse ikili esik degeri
_, im = cv2.threshold(im, 120, 255, cv2.THRESH_BINARY_INV)
plt.subplot(2, 2, 2)
plt.imshow(im, cmap="gray")

im = cv2.morphologyEx(im, cv2.MORPH_OPEN, np.ones([3, 3]))  # gurultuden kurtul
# _, comp = cv2.connectedComponents(im)  # connected components analizi
# bu kismi kendimiz gercekleyelim.


def connectedComponents(im):
    """ Custom connected component analysis """
    connectivity = [
        [-1, -1], [-1, 0], [-1, +1],
        [0, -1], [0, +1],
        [1, -1], [1, 0], [1, +1]
    ] # komsuluk/connectivity matrisi
    shape = im.shape

    def setLabelRec(im, point, label):
        """ Recursive utility function for CCA """
        im[point[0]][point[1]] = label
        # bu pikseli etiketle
        for offset in connectivity:
            # etraftaki pikseller icin
            y = point[0] + offset[0] # y noktasi
            x = point[1] + offset[1] # x noktasi
            if y < 0 or y >= shape[0] or x < 0 or x >= shape[1]:
                continue # eger goruntunun disina tasildiysa, atla
            if im[y][x] == 255: # eger cevredeki piksel beyaz ise etiketle
                setLabelRec(im, (y, x), label) # rekursif cagri

    label_counter = 0 # etiket sayaci
    white = np.argwhere(im == 255) 
    # goruntudeki beyaz olan yerlerin koordinatlarini al
    while len(white) > 0:
        # eger beyaz bir nokta varsa
        setLabelRec(im, white[0], label_counter) 
        # beyaz noktayi etiketle, rekursif bicimde
        white = np.argwhere(im == 255) # beyaz nokta listesini guncelle
        label_counter += 1 # etiket sayacini arttir

    return im


comp = connectedComponents(im)
plt.subplot(2, 2, 3)
plt.imshow(im, cmap="gray")

plt.subplot(2, 2, 4)
plt.imshow(comp, cmap="nipy_spectral")

plt.show()