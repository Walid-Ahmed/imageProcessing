
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

numberOfFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( "[INFO] The video includes {0} frames".format(numberOfFrames))
fps = cap.get(cv2.CAP_PROP_FPS)
print ("[INFO] Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
print("[INFO] while playing press  p to pause, press r to resume and press q to quit ")


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
    

    # record key press
    key = cv2.waitKey(10) & 0xFF
        
    if key== ord('q'):  # press q to quit  video play back
        break
        
    if key == ord('p'):       
        while (True):
            key = cv2.waitKey(10) & 0xFF
            if key== ord('r'):  # press r  to continute  video play back
                break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Extracted frames saved to folder {}".format(folderNameToSaveFrames))

