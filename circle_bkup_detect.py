import cv2
import numpy as np
import os
import picamera
import sys
import picamera.array
import time

sys.path.append('/usr/local/lib/python3.4/site-packages')
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate =32
rawCapture = picamera.array.PiRGBArray(camera, size=(640,480))
time.sleep(0.5)
i = 0
j = 0

for frame in camera.capture_continuous(rawCapture, format="bgr" , use_video_port=True):
     img = frame.array   
     img = cv2.medianBlur(img,5)
     cv2.imshow("image",img)
     key = cv2.waitKey(2) & 0xFF
     rawCapture.truncate(0)
     if key == ord("q"):
         break
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
     count = 0
     edge = cv2.Canny(img,100,200)
##cv2.imshow("edged",edge)
#cv2.waitKey(10)
#cv2.destroyAllWindows()
#edge = cv2.imread("/Users/bharath/Downloads/project/frame13.jpg")

     circles = cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=40,maxRadius=100)
                            

                            

     try:
    
       circles = np.uint16(np.around(circles))
       for i in circles[0,:]:
        # draw the outer circle
        count = count + 1
        print ("Center Coordinates", i[0],i[1])
        if (count <= 1):
             cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
             cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
             print ("Center Coordinates", i[0],i[1])
             cv2.imshow('detected circles',img)
             cv2.waitKey(10)
             cv2.destroyAllWindows()
             cv2.imwrite("/home/pi/Desktop/EC601_door/ip/output/pic{:>15}.jpg".format(j),img)
             j = j+1

     except AttributeError:
       print (" Not able to detect the radius")
       #continue
       
