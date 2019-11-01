# cd /Users/walidahmed/Desktop/Code/TensorFlow_ObjectDetection/models-master/object_detection
#python object_detection_video.py
# coding: utf-8

# # Object Detection Demo
# Welcome to the object detection inference walkthrough!  This notebook will walk you step by step through the process of using a pre-trained model to detect objects in an image. Make sure to follow the [installation instructions](https://github.com/tensorflow/models/blob/master/object_detection/g3doc/installation.md) before you start.

# # Imports

# In[2]:


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
from IPython import get_ipython
import cv2





#from utils import visualization_utils as vis_util

folder="/Volumes/W/ML_frames_Demo11"
folder="/Users/walidahmed/Desktop/Demos/PersonsWithDetection_Demo10"   #RFCN
folder="/Users/walidahmed/Desktop/code/visualization_tools/Demo3/ML_frames"
folder="/Users/walidahmed/Downloads/ML_frames_noInfo"
folder="/Users/walidahmed/Downloads/eval/concreteworker"
scaleFactor=0.6
width=130#1920
height=400#1080
width=int(width*scaleFactor)
height=int(height*scaleFactor)
filenamesList=os.listdir(folder)
fourcc = cv2.VideoWriter_fourcc(*'H264')
fileName="indus.ai_privacy_mask_ETF_v5C.mp4"
fileName="concreteworker.mp4"
video_creator = cv2.VideoWriter(fileName,fourcc, 30, (1280,780))

def  showVideo():
    		frameNum=1
    		while(frameNum<23300):
    		#for filename in filenamesList:
				filename="ml_frame_"+str(frameNum)+".png"   
				print(filename)
				img = cv2.imread(os.path.join(folder,filename))
				#img = cv2.resize(img, (width, height)) 
				if (img is None):
					frameNum=frameNum+1
					continue
				img=cv2.resize(img,(1280,780))
				video_creator.write(img)
				cv2.imshow('indus.ai',img)
				#if (frameNum==1):
					#raw_input("press any key to continue")
				cv2.waitKey(1)
				frameNum=frameNum+1
				#out.write(img)
				print(frameNum)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
    	 		


#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter("Detect_HardHat.m4v",fourcc, 5, (1152,648))
showVideo()
video_creator.release()







