#python videoPlayBackFromFiles.py --folderPath ZakiBashakha


import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import  pyplot  as plt
from PIL import Image
import cv2
import argparse





def  showVideofromFrames():
    		frameNum=1
    		for filename in imgFiles:
    			print(filename)
    			img = cv2.imread(os.path.join(folderPath,filename))
    			#img = cv2.resize(img, (width, height)) 
    			if (img is None):
    				frameNum=frameNum+1
    				continue
    			img=cv2.resize(img,(width,height))
    			video_creator.write(img)
    			cv2.imshow(folderPath,img)
				#if (frameNum==1):
					#raw_input("press any key to continue")
    			cv2.waitKey(1)
    			frameNum=frameNum+1
    			#out.write(img)
    			if cv2.waitKey(1) & 0xFF == ord('q'):
    				break
    	 		





#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter("Detect_HardHat.m4v",fourcc, 5, (1152,648))
    #read the arguments


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("--folderPath", required=True,help="path to frames  of video")

    args = vars(ap.parse_args())
    folderPath=args["folderPath"]

    scaleFactor=0.6
    width=1280
    height=720
    width=int(width*scaleFactor)
    height=int(height*scaleFactor)
    filenamesList=os.listdir(folderPath)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fileName="demo.mp4"

    video_creator = cv2.VideoWriter(fileName,fourcc, 2, (width,height))
    imgFiles=os.listdir(folderPath)
    imgFiles.sort()
    imgFiles=sorted(os.listdir(folderPath))

    showVideofromFrames()
    video_creator.release()
    print("[INFO] Video file created  and saved to {}".format(fileName))







