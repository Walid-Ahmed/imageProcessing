#usage
#python videoPlayBack.py--videoFilePath videos/CarsDrivingUnderBridge.mp4
#Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

import numpy as np
import cv2
import imutils
import os
import argparse







if __name__ == "__main__":

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("--videoFilePath", required=True, help="path to video file")


    #read the arguments
    args = vars(ap.parse_args())
    videoFilePath=args["videoFilePath"]


    cap = cv2.VideoCapture(videoFilePath)
    numberOfFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( "[INFO] The video includes {0} frames".format(numberOfFrames))
    numberOfProcessedFrames=0
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("[INFO] Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    print("[INFO] while playing press p to pause, press r to resume and press q to quit ")

    input("Press any key to start playing video")


    frameNum=0
    while(cap.isOpened()):
        

        ret, frame = cap.read()
        #print(frame)
        if (frame is None):
            frameNum=frameNum+1
            break

        frameNum=frameNum+1
        frame = imutils.resize(frame, width=500, height=280)
        print("frame Num {0} read sucessfully".format(frameNum))
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
