#!/bin/python

import cv2
import os
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

#########
#Parameters
#stack directory
imdir="/home/friedrichsenk/TestImageStack/"
#what are the stack files?
imgtype='.png'
#outputfilename
outputfile='testout3.txt'

#get a list of the png files in the directory
imlist=[s for s in os.listdir(imdir) if s.endswith(imgtype)]
imlist.sort()
#open the output
output=open(outputfile,"w")
#create empty array for results
totalFlow=[]
#set up the initial frame
previous = cv2.imread(imlist[0])
previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)

#loop through the images in the stack
for i in range(len(imlist)):
  #get the filename
  imfile=imlist[i]
  #open the file
  frame1 = cv2.imread(imfile)
  #convert it to grayscale; it's already in grayscale
  frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
  #set the final frame
  frame=frame2
  #calculate the OF from the previous frame
  #this returns a list of the xy vectors for each displacement
  flowRA = cv2.calcOpticalFlowFarneback(previous, frame, None ,0.5, 3, 15, 3, 5, 1.1, 0)
  #add that to the results
  totalFlow.append(flowRA)
  #get the test pixel displacement
  testflow=np.array(flowRA[1024,768])
  #create sequential array
  intRA=[i+1 for i in range(1920)]
  #create the adnaus repeats
  xRA=intRA
  yRA=intRA[0:1080]
  #flowRA=np.transpose(flowRA,(1,0,2))
  sleep(0.5)
  #~ print(flowRA.shape)
  #~ print("flowRAlen")
  #~ print(len(flowRA))
  #~ print(type(flowRA))
  #~ print("flowRA[0]len")
  #~ print(len(flowRA[0]))
  #~ print(type(flowRA[0]))
  #~ print("flowRA[0,0]len")
  #~ print(len(flowRA[0,0]))
  #~ print(type(flowRA[0,0]))
  #~ print(flowRA[0,0,0])
  #Need to get the values from the thing into a form for graphing
  for y in range(len(flowRA)):
    for x in range(len(flowRA[0])):
      dxy=np.array(flowRA[y,x])
      dxy=dxy*10
      #print(dxy)
      xy=(np.array([y,x]))
      xydif=np.round(xy+dxy,0)
      posxy=tuple(xy)
      #print(xydif)
      posdxy=tuple([int(xydif[0]),int(xydif[1])])
      #print(posdxy)
      plotarrowtest=cv2.arrowedLine(frame,posxy,posdxy,(255,0,0),3)
      frame = cv2.add(frame,plotarrowtest)
  #~ plotarrowtest=cv2.arrowedLine(frame,(1024,768),(int(round(1024+testflow)),int(round(768+testflow))),(255,0,0),3)
  cv2.imshow('frame',frame)
  
  #write results for test pixel 
  #~ output.write(np.array_str(flowRA[1024,768]))
  
  #I don't know what these do
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break
  #set the previous to the current frame for next iteration
  previous=frame
output.close()
cv2.destroyAllWindows()
#~ plt.show()

#~ totalFlow
  #~ sleep(0.5)

#~ cv2.destroyAllWindows()
