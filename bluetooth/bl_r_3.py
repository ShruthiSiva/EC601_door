import serial
import pyuarm
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input5.jpg',0)
img2 = img.copy()
template = cv2.imread('canny_multi_temp_output.jpg',0)
w, h = template.shape[::-1]
w1, h1 = img.shape[::-1]
dpi = 72
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

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
    
    #print(top_left)
    #print (bottom_right)

    a = cv2.rectangle(img,top_left, bottom_right, 255, 2)
    cx = (top_left[0]+ bottom_right[0])*25.4/(2*dpi)
    cy = (top_left[1] + bottom_right[1])*25.4/(2*dpi)
    
    print (cx)
    print (cy)
        

#    plt.subplot(121),plt.imshow(res,cmap = 'gray')
#    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle('meth')
    cv2.imwrite('/Users/bharath/Downloads/project/match_opt2.jpg',img)

#plt.show()

#Uarm commands
uarm = pyuarm.get_uarm()
ch = w1*25.4/(2*dpi)
cv = h1*25.4/(2*dpi)
print(ch)
print(cv)
x, y, z = uarm.get_position()
print(x)
print(y)
print(z)
print("difference")
print(cx-ch)
print(cy-cv)
uarm.set_position(x - abs(cx-ch),y,z - abs(cy-cv))
x, y, z = uarm.get_position()
print(x)
print(y)
print(z)
#ofh = ch - '''
plt.show()

uarm.disconnect()
#uarm.dettach()