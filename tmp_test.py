# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:45:39 2016

@author: bharath
"""

import cv2
import numpy as np

img_rgb = cv2.imread('template3.jpg')
#cv2.resize(img_rgb,(0,0),fx=0.5,fy=0.5)
#cv2.imshow('Resize',img_rgb)
#cv2.waitKey(1000)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.78
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

#cv2.namedWindow('Detected', cv2.WINDOW_NORMAL)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)