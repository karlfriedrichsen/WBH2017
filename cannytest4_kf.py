import cv2
import numpy as np
import os
from time import sleep

imdir="/home/friedrichsenk/TestImageStack/"
imlist=[s for s in os.listdir(imdir) if s.endswith('.png')]

for i in range(len(imlist)):
    imfile=imlist[i]
    frame1 = cv2.imread(imfile, 0)
    frame=cv2.equalizeHist(frame1)
    #~ _, frame = cap.read()
    #~ hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #~ lower_red = np.array([30,150,50])
    #~ upper_red = np.array([255,255,180])
    
    #~ mask = cv2.inRange(hsv, lower_red, upper_red)
    #~ res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    sleep(1)
cv2.destroyAllWindows()
cap.release()
