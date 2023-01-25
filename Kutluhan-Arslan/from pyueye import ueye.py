from pyueye import ueye
import cv2

h_cam = ueye.HIDS(0)



ret = ueye.is_InitCamera(h_cam, None)

kamera = ueye.is_CaptureVideo(0, 1)

cv2.namedWindow("goruntu", cv2.WINDOW_NORMAL)

cv2.imshow("goruntu",kamera)
        
        



cv2.waitKey(0)