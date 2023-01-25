from pyueye import ueye


while True:
    

    h_cam = ueye.HIDS(0)
    ret = ueye.is_InitCamera(h_cam, None)
    

    print(ret)


    if ret != ueye.IS_SUCCESS:
        pass