import cv2
import numpy as np
import os
#img = cv2.imread('/Users/bharath/Desktop/IMG_3598.jpg')
#print (img)
#cv2.imshow("Input",img)

cap = cv2.VideoCapture(0)
frameRate = cap.get(5)
i = 0
template = cv2.imread('/Users/bharath/Downloads/project/template.jpg')
#w, h = temp.shape[::-1]
method = cv2.TM_CCOEFF_NORMED
#while(1):
while(cap.isOpened):
    frameId = cap.get(1)
    channels,img = cap.read(0)
    img = cv2.medianBlur(img,5)
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
#             for jj in range (i[0],i[1]):
#                     res = cv2.matchTemplate(img,template,method)
#                     #print (res)
#                     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#                     #print (max_val)
#                     top_left = max_loc
#                     bottom_right = (top_left[0], top_left[1])
#                     if (max_val == 0.85):
#                            cv2.rectangle(img,top_left, bottom_right, (255,0,0), 2)
#             while os.path.exists("sample%s.xml" % i):
#                i += 1
#                cv2.imwrite("sample%s.xml" % i,img)
             
      
       cv2.imshow('detected circles',img)
       cv2.waitKey(10)
       cv2.destroyAllWindows()

    except AttributeError:
       print (" Not able to detect the radius")
       #continue
       
