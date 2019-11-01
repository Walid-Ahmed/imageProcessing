import numpy as np
import cv2
import imutils

alpha=0.5
def clear():
    global  framenum 
    framenum=0

    
newWidth=500
newHeight=380
cap = cv2.VideoCapture('CarsDrivingUnderBridge.mp4')
#cap = cv2.VideoCapture('SampleVideo.mp4')
framenum=0
#cap = cv2.VideoCapture(0)
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=newWidth, height=newHeight)
    overlay = frame.copy()
    framenum=framenum+1
    
 

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame, (0, newHeight-60), (newWidth, newHeight),(0, 0, 255), -1)
    cv2.putText(frame,"Zizo:"+str(framenum), (30,newHeight-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)

    #cv2.addWeighted(overlay, alpha, frame, 1 - alpha,0, frame)


    
    cv2.imshow('frame',frame)
    cv2.waitKey(25)
    key=cv2.waitKey(1) #& 0xFF 
    if key== ord('r') or key== ord('R'):
        clear()
    if key== ord('q') or key== ord('Q'):
        break    
        
        

cap.release()
cv2.destroyAllWindows()


def clear():
    framenum=0
    
'''    
cv2.imshow('frame', frame)
key = cv2.waitKey(1)
if key == 17:        # Ctrl+Q or ^Q
    break    
 http://academic.evergreen.edu/projects/biophysics/technotes/program/ascii_ctrl.htm   
'''    