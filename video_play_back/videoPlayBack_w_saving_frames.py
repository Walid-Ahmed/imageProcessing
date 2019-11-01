
#cd video_play_back/
#python  video_play_back/videoPlayBack_w_saving_frames.py   --fileName videos/CarsDrivingUnderBridge.mp4 --everyNFrame 1

#Frames will be samples everyNFrame and saved to a folder with the same name as the video file name


import numpy as np
import cv2
import os
import shutil
import argparse



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--fileName", required=True,help="path to video file")
ap.add_argument("--everyNFrame", default=1,help="path to input image")



args = vars(ap.parse_args())

fileName=args["fileName"]
everyNFrame=int(args["everyNFrame"])

folderNameToSaveFrames=(os.path.basename(fileName))[:-4]


cap = cv2.VideoCapture(fileName)
shutil.rmtree(folderNameToSaveFrames, ignore_errors=True, onerror=None)
os.makedirs(folderNameToSaveFrames)


frameNum=0


print("[INFO] Saving  a frame from every {} frames from video file {} ".format(everyNFrame,fileName))
input("press any key to continue")
while(cap.isOpened()):
    ret, frame = cap.read()
    if (frame is None):
        break
    if(frameNum%everyNFrame==0):
        fileNameToSaveFrame=os.path.join(folderNameToSaveFrames, folderNameToSaveFrames+"_"+str(frameNum)+".png")
        cv2.imwrite(fileNameToSaveFrame, frame)
        print("[INFO] frame#  {}  saved to  {}".format(frameNum,fileNameToSaveFrame))
    else:  
        print("[INFO]  frame# {}  skipped and not saved".format(frameNum))
  
    
    
    frameNum=frameNum+1


    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print("[INFO] Extracted frames saved to folder {}".format(folderNameToSaveFrames))

