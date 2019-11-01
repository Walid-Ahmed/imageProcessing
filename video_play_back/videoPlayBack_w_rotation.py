import numpy as np
import cv2
import imutils
import os


fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case

fileName="sample.mp4"
videoFileName=os.path.join("videos",fileName)
cap = cv2.VideoCapture(videoFileName)
width=cap.get(3) #width
height=cap.get(4) #height
print(width,height)
print ("[INFO] Width  {0} and Height {1} for video".format(width,height))
fps = cap.get(cv2.CAP_PROP_FPS)
print ("[INFO] Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))



fileNameToSave="rotated_"+fileName
video_creator = cv2.VideoWriter( fileNameToSave, fourcc, fps, (int(height),int(width))  )





#fps    = cap.get(cv2.CAP_PROP_FRAME_COUNT)
#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
#print("FRAME_Per_Second",fps)

frameNum=0
while(cap.isOpened()):
    

    ret, frame = cap.read()
    #print(frame)
    if (frame is None):
        frameNum=frameNum+1
        break
    	
    frameNum=frameNum+1
    frame = imutils.resize(frame, int(width), int(height))
    frame = imutils.rotate_bound(frame, 90)
    height, width = frame.shape[:2]
    print ("[INFO]  Saving frame wuth Width  {0} and Height {1} for video".format(width,height))


    video_creator.write(frame)



   
    print("Showing frame number {0}".format(frameNum)) 

    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    key = cv2.waitKey(1)
    
    if key == 17:        # Ctrl+Q or ^Q
    	raw_input("press any key to continue")

    	#break
video_creator.release()
cap.release()
cv2.destroyAllWindows()
