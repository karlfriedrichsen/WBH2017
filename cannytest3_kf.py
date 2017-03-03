import cv2
import numpy as np
import os
from time import sleep

imdir="/home/friedrichsenk/TestImageStack/"
imlist=[s for s in os.listdir(imdir) if s.endswith('.png')]

for i in range(len(imlist)):

    # Take each frame
    #_, frame = imread.
    imfile=imlist[i]
    frame1 = cv2.imread(imfile, 0)
    
    #~ hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.equalizeHist(frame1)
    
    #~ lower_red = np.array([30,150,50])
    #~ upper_red = np.array([255,255,180])
    
    #mask = cv2.inRange(hsv, lower_red, upper_red)
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    #laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    #~ sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=3)

    cv2.imshow('Original',frame)
    #~ cv2.imshow('Mask',mask)
    #cv2.imshow('laplacian',laplacian)
    #~ cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    sleep(1)

cv2.destroyAllWindows()
cap.release()
