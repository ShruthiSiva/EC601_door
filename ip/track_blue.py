
############################################
## Import OpenCV
import numpy as np
import cv2
i = 0
cap = cv2.VideoCapture(1)
'''
while i <100:
    _, frame = cap.read()
    i = i+1
'''
while(1):
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
    lower_yellow = np.array([100, 100, 100])
    upper_yellow = np.array([139, 255, 255])
        
        # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    kernel = np.ones((20,20),np.uint8)
        #opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    #edges = cv2.Canny(img,100,150)
    #ret,thresh2 = cv2.threshold(edges,127,255,cv2.THRESH_BINARY_INV)
    gray = opening
    img = frame
    cv2.imshow('Original',img)

    #i = 2
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    n = len(contours)
    print n
    if n != 0:
        
        #for i in len(contours):
        myList=[]
        for i in range(n):
            myList.append(cv2.contourArea(contours[i]))
        
        print "Area = ", max(myList)
        largest = myList.index(max(myList))
        print "Perimeter = ", cv2.arcLength(contours[largest],True)
        M = cv2.moments(contours[largest])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #print "Centroid = ", cx, ", ", cy
        #cv2.circle(img,(cx,cy), 5, (255,0,255), -1)
        #cv2.drawContours(img,contours,largest,(255,0,0),2)
        ############################################
        cnt=contours[largest]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cx = x + w/2
        cy = y + h/2
        cv2.circle(img,(cx,cy), 5, (255,0,255), -1)
        
        ############################################
        ## Show the image
        cv2.imshow('opening',opening)
        cv2.imshow('image',img)
    ############################################
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    ############################################
    ## Close and exit
cv2.destroyAllWindows()
############################################
