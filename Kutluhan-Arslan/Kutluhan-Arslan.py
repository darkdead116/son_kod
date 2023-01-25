import cv2
import numpy as np 
from pyueye import ueye
import sys



def kamera_video():
    
    h_cam = ueye.HIDS(0)
    
    
    
    while True:
        
        ret = ueye.is_InitCamera(h_cam, None)
        
        kamera= ueye.is_CaptureVideo(h_cam,1)

        cv2.imshow("görüntü",kamera)       

        cv2.namedWindow("video", cv2.WINDOW_NORMAL)
            
        cv2.waitKey(0)
    
    
    
if __name__ == '__main__':
    
    kamera_video()
    