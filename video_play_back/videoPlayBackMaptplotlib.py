import cv2
import matplotlib.pyplot as plt

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

#Initiate the two cameras
#cap1 = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)

fileName="GOBox_CD_T_Gate_2017-03-17-17.21.59.591-UTC_141_2017-03-20-15.52.40.104-UTC.mp4"
cap1 = cv2.VideoCapture(fileName)
_, ax = plt.subplots()

im = ax.imshow(grab_frame(cap1))




plt.ion()

while True:
    #im1.set_data(grab_frame(cap1))
    #im2.set_data(grab_frame(cap2))
    im.set_data(grab_frame(cap1))

    plt.pause(0.2)

plt.ioff() # due to infinite loop, this gets never called.
plt.show()