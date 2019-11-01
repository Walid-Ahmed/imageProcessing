import cv2 as cv
import os
import numpy as np

class VideoMontage:


  def __init__(self):
    self.width,self.height=150,225
    self.frame = np.zeros((900, 900, 3), np.uint8) #6 videos in row. 4 videos in columns. (total 24)
    self.videoPathsGenerator=self.getListOfvideoFiles()
    self.videoPaths=os.listdir("videos")
    self.videoPaths.sort()
    self.cap=[None] * 24

    self.cap[0]=9



  
  def  getListOfvideoFiles(self):


    for filePath in self.videoPaths :
      yield  filePath




   

  def run(self):
    fourcc = cv.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    fileNameToSaveVideo="demo_Video.mp4"
    video_creator = cv.VideoWriter(fileNameToSaveVideo,fourcc, 20, (900,900))
   

    for i in range(24):
          #print(i)
          try:
            fileName=next(self.videoPathsGenerator)
            fileName=os.path.join("videos",fileName)
            (self.cap)[i] = cv.VideoCapture(fileName)
            print("[Info] cap {}  opened to file {}".format(i,fileName))
          except:
            exit()
            
    h,w=self.height,self.width
    while True:
      row=0
      for i in range(24):
          #print(i)
          try:

            ret, img = self.cap[i].read()
            #img = cv.resize(img,(self.width,self.height))

            if (img is None):
              try:
                  fileName=next(self.videoPathsGenerator)
                  (self.cap)[i] = cv.VideoCapture(os.path.join("videos",fileName))
                  ret, img = self.cap[i].read()
              except:
                  print("[ERRRO] No more files to display "+ str(e))
                  img=np.zeros(self.width,self.height)  # No more files show white screen

                 #reintialize with a new video
              print("[Info] Cap {} Video ReInitialized to {}".format(i,os.path.join("videos",fileName)))
            


            ''' 
            if not ret:   # No more frames in current cap
               try:
                  fileName=next(self.videoPathsGenerator)
                  (self.cap)[i] = cv.VideoCapture(fileName)
               except:
                  print("[ERRRO] No more files to display "+ str(e))
                  img=np.zeros(self.width,self.height)

                 #reintialize with a new video
               print ("[info]Video Initialized")
            '''

            x1=0+(i%6)*150
            y1=self.height*row  


            #print("Image {} at coordinates x1={} ,y1= {}, x2={},y2={}. at row {}".format(i,x1,y1,x1+w,y1+h,row))
            try: 
              img = cv.resize(img,(self.width,self.height))
            except:
              print(img.shape)
              input("Can not resize")
              exit()
              
            
            self.frame[y1:y1+self.height, x1:x1+self.width]=img   
            
            if (x1==750):
              row=row+1

            '''

            if (i==0):
                  x1,y1,h,w=0,0,self.height,self.width
                  print(y1,y1+h, x1,x1+w)
                  self.frame[y1:y1+h, x1:x1+w]=img  
            if (i==1):
                  x1,y1,h,w=150,150,self.height,self.width
                  self.frame[y1:y1+h, x1:x1+w]=img   

            '''


                      





          except Exception as e:     
            print(str(e.__class__.__name__))
            print("[ERRRO] No more files to display "+ str(e))
            video_creator.release()
            exit()
            break
      
      cv.imshow('Video Montage',self.frame)
      video_creator.write(self.frame)
      k = cv.waitKey(10) 
      if k == 27:
          break      

    video_creator.release()

if __name__ == "__main__":
  videoMontage=VideoMontage()
  videoMontage.run()


