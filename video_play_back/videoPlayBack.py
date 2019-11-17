#usage
#python videoPlayBack.py--videoFilePath videos/CarsDrivingUnderBridge.mp4

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

    width=cap.get(3) #width
    height=cap.get(4) #height
    ret=cap.set(3,300) 
    ret=cap.set(4,300)

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
        frame = imutils.resize(frame, width=500, height=280)
        print("frameNum {0} read sucessfully".format(frameNum))
        frameNum=frameNum+1



        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        key = cv2.waitKey(1)
        
        if key == 17:        # Ctrl+Q or ^Q
        	raw_input("press any key to continue")
        	#break

    cap.release()
    cv2.destroyAllWindows()
