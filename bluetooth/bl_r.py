import serial
import pyuarm
import cv2
import numpy as np
from matplotlib import pyplot as plt

ser = serial.Serial('COM18')  # open serial port
#print(ser.name)         # check which port was really used
#ser.open()
x = ser.read(2)
#print(x)
if (x==x):
    print('Open Request Received')
ser.close()


#IP
input=cv2.imread('input4.jpg',0)
edges=cv2.Canny(input,100,200)
cv2.imwrite('output.jpg',edges)
img = cv2.imread('output.jpg',0)
img2 = img.copy()
template = cv2.imread('canny_multi_temp_output.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = cv2.TM_CCOEFF
    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    cv2.imwrite('match_opt4.jpg',img)
plt.show()
    #print("shown")
    



#Uarm commands
uarm = pyuarm.get_uarm()
uarm.set_position(0,300,170)
uarm.disconnect()
#uarm.dettach()
