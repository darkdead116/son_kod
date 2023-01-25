from tkinter import *
from tkinter import ttk
import turtle
import cv2
from PIL import Image, ImageTk
import sys




width =600
height = 600

pencere = Tk()

pencere.title("arayüzpencere")
pencere.geometry("1200x1200")

uygulama = Frame(pencere)
uygulama.pack()

pencere0 = Scale(pencere, from_ =0, label= "Expourse değeri", to= 20000, orient= HORIZONTAL )
pencere0.pack(side= "bottom")

pencere1 = Scale(pencere, from_ =0, label= "Brightness değeri", to= 255, orient= HORIZONTAL )
pencere1.pack(side= "bottom")

pencere2 = Scale(pencere, from_ =0, label= "Contrast değeri", to= 255, orient= HORIZONTAL )
pencere2.pack(side= "bottom")

pencere3 = Scale(pencere, from_ =0, label= "FPS değeri", to= 60, orient= HORIZONTAL )
pencere3.pack(side= "bottom")



capture = cv2.VideoCapture(1)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#capture.set(cv2.CAP_PROP_FRAME_FPS, pencere3.Scale.value)
#capture.set(cv2.CAP_PROP_FRAME_BRIGHTNESS, pencere1)
capture.set(cv2.CAP_PROP_EXPOSURE, pencere0.get())

pencere.bind('<Escape>', lambda e: pencere.quit())

label_widget = Label(pencere)
label_widget.pack()

def open_camera():

    _, frame = capture.read()

    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image

    label_widget.configure(image=photo_image)

    label_widget.after(10, open_camera)
    

def sistemi_durdur():

    print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("CAP_PROP_FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
    print("CAP_PROP_POS_MSEC : '{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))
    print("CAP_PROP_FRAME_COUNT  : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("CAP_PROP_BRIGHTNESS : '{}'".format(capture.get(cv2.CAP_PROP_BRIGHTNESS)))
    print("CAP_PROP_CONTRAST : '{}'".format(capture.get(cv2.CAP_PROP_CONTRAST)))
    print("CAP_PROP_SATURATION : '{}'".format(capture.get(cv2.CAP_PROP_SATURATION)))
    print("CAP_PROP_HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
    print("CAP_PROP_GAIN  : '{}'".format(capture.get(cv2.CAP_PROP_GAIN)))
    print("CAP_PROP_CONVERT_RGB : '{}'".format(capture.get(cv2.CAP_PROP_CONVERT_RGB)))
    sys.exit()

button1 = Button(pencere, text="Open Camera", command=open_camera)
button1.pack()




mainloop()

cv2.destroyAllWindows()
cv2.waitKey(0)
