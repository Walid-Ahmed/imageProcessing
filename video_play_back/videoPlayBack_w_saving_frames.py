import numpy as np
import cv2
import os
import shutil




fileName="videos/lorex-20181217-143851-144310.mp4"
folderNameToSaveFrames=(os.path.basename(fileName))[:-4]




cap = cv2.VideoCapture(fileName)
shutil.rmtree(folderNameToSaveFrames, ignore_errors=True, onerror=None)
if not os.path.exists(folderNameToSaveFrames):
    			os.makedirs(folderNameToSaveFrames)

width=cap.get(3) #width
height=cap.get(4) #height
#ret=cap.set(3,300) 
#ret=cap.set(4,300)
#fps    = cap.get(cv2.CAP_PROP_FRAME_COUNT)
#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
#print("FRAME_Per_Second",fps)

print (width,height)
fps = cap.get(cv2.CAP_PROP_FPS)
print ("Frames per second  : {0}".format(fps))
frameNum=0
numberOfFramesPerSecondtoSave=6
everyNFrame=int(fps)*2
everyNFrame=int(fps/numberOfFramesPerSecondtoSave)

everyNFrame=5
print("Saving  a frame from every {0} frames ".format(everyNFrame))
raw_input("press any key to continue")
while(cap.isOpened()):
    ret, frame = cap.read()
    if (frame is None):
	break
    if(frameNum%everyNFrame==0):
    	cv2.imwrite(os.path.join(folderNameToSaveFrames, folderNameToSaveFrames+"_"+str(frameNum)+".png"), frame)
    	print("framed saved to  "+ "frame"+"_"+str(frameNum)+".png")
    
    
    
    
    
    #cv2.imwrite("frame"+"_"+str(i)+".png", frame)
    
    frameNum=frameNum+1
    print(frameNum)


    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
