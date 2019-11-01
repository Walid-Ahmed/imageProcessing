import numpy as np
import cv2
import imutils

x1_box=90
y1_box=68
x2_box=260
y2_box=120
r=255
blue=0

def drawVirtualLine(frame,blue,red):
    cv2.rectangle(frame, (x1_box, y1_box), (x2_box, y2_box), (0, blue, red), 1) #crossing line
    r=255
    blue=0

def getROI(frame):
 	gate=frame.copy()
 	gate=gate[y1:y2,x1:x2]
 	drawVirtualLine(gate,blue,r) 
 	return gate

#cap = cv2.VideoCapture('IndusAI SR_Intersection 20160731 1412.mp4')
#cap = cv2.VideoCapture('video_test.mp4')
folder="/Users/walidahmed/Desktop/"
fileName="GOBox_CD_T_Gate_2017-03-17-17.21.59.591-UTC_141_2017-03-20-15.52.40.104-UTC.mp4"
src=folder+fileName

cap = cv2.VideoCapture(src)
newWidth=500
newHeight=281
width=cap.get(3) #width
height=cap.get(4) #height
ret=cap.set(3,300) 
ret=cap.set(4,300)
#fps    = cap.get(cv2.CAP_PROP_FRAME_COUNT)
#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
#print("FRAME_Per_Second",fps)

x1=100
x2=400
y1=64
y2=280
r=255
blue=0


while(cap.isOpened()):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=newWidth, height=newHeight)
    gate=getROI(frame)
   
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('indus.ai',frame)
    cv2.imshow('Gate',gate)


    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


