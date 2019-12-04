#python videoMontage.py --rows 4 --cols 6 


import cv2 
import os
import numpy as np
import paths
import argparse

class VideoMontage:


  def __init__(self,rows=4,cols=6):
    self.rows,self.cols=rows,cols
    self.numToShow=self.rows*self.cols
    self.width,self.height=int(900/cols),int(900/rows)
    self.frame = np.zeros((900, 900, 3), np.uint8) 
    self.videoPathsGenerator=self.getListOfvideoFiles()
    self.videoPaths=paths.list_videos("videos")
    self.cap=[None] * self.numToShow



  
  def  getListOfvideoFiles(self):
 
    for filePath in self.videoPaths :
      yield  filePath




   

  def run(self):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    fileNameToSaveVideo="demo_Video.mp4"
    video_creator = cv2.VideoWriter(fileNameToSaveVideo,fourcc, 60, (900,900))
   

    for i in range(self.numToShow):
          #print(i)
          try:
            fileName=next(self.videoPathsGenerator)
            (self.cap)[i] = cv2.VideoCapture(fileName)
            print("[Info] cap {}  opened to file {}".format(i,fileName))
          except:
            print("[ERROR] Not enough videos to start, add more videos to videos folder")
            print("[ERROR] program exited")
            exit()
    
    print("[INFO]  initial {} videos loaded sucessfully".format(self.numToShow))     

    h,w=self.height,self.width

    while True:
      row=0
      numEmpty=0
      for i in range(self.numToShow):
          #print(i)
          try:
            print("----------------------------")
            ret, img = self.cap[i].read()
            print("Cap {} opened  sucessfully".format(i))

            if (img is None):   #video reached end frame
              try:
                  fileName=next(self.videoPathsGenerator)
                  (self.cap)[i] = cv2.VideoCapture(fileName)     #get a new video
                  ret, img = self.cap[i].read()
                  print("[Info] Cap {} Video reinitialized to {}".format(i,fileName))
              except:
                  print("[ERRRO] No more files to display, a  white screen is shown in this cell  ")
                  #img=np.ones((self.width,self.height))  # No more files show white screen
                  img=255*np.ones((self.height,self.width,3))  # No more files show white screen
                  text = 'N/A'
 
                  # org 
                  org = (int(self.width/4),int(self.height/4)) 
                    

                  # Using cv2.putText() method 
                  cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) , 1, cv2.LINE_AA, False) 
                  numEmpty=numEmpty+1
  




            x1=0+(i%self.cols)*self.width
            y1=self.height*row
            img = cv2.resize(img,(self.width,self.height))
            self.frame[y1:y1+self.height, x1:x1+self.width]=img  

            
            if (x1==(900-self.width)):
              row=row+1
      


          except Exception as e:   
            print(e)  
            break

            
      
      cv2.imshow('Video Montage',self.frame)
      video_creator.write(self.frame)

      if(numEmpty==self.numToShow):
          break
      
      key = cv2.waitKey(1) & 0xFF

      # if the `q` key was pressed, break from the loop
      if key == ord("q"):
        break  

     
    video_creator.release()

if __name__ == "__main__":

  # construct the argument parser and parse the arguments
  ap = argparse.ArgumentParser()
  ap.add_argument("-m", "--rows",
    help="path to BING objectness saliency model")
  ap.add_argument("-i", "--cols", required=True,
    help="path to input image")

  args = vars(ap.parse_args())
  rows=int(args["rows"])
  cols=int(args["cols"])


  videoMontage=VideoMontage(rows,cols)
  videoMontage.run()



