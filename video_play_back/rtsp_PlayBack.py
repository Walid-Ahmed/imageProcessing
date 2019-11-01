import numpy as np
import cv2

#cap = cv2.VideoCapture('IndusAI SR_Intersection 20160731 1412.mp4')
#cap = cv2.VideoCapture('video_test.mp4')
cap = cv2.VideoCapture('rtsp://admin:greenowl123@192.168.0.117')
ret, frame = cap.read()
print(ret)

'''
width=cap.get(3) #width
height=cap.get(4) #height
ret=cap.set(3,300) 
ret=cap.set(4,300)

fps    = cap.get(cv2.CAP_PROP_FRAME_COUNT)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
print("FRAME_Per_Second",fps)
'''

while(True):
    ret, frame = cap.read()
    print frame.shape
    print ret
    ret=cap.set(3,300) 
    ret=cap.set(4,300)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
