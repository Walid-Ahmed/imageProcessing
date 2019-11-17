# imageProcessing
image Processing using python

## Video playback 

Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

cd video_play_back </br>
python videoPlayBack.py --videoFilePath videos/CarsDrivingUnderBridge.mp4


## Video play back while saving sample frames

Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

cd video_play_back/  </br>
python  videoPlayBack_w_saving_frames.py   --fileName videos/CarsDrivingUnderBridge.mp4 --everyNFrame 1

Frames will be sampled every N Frame and saved to a folder with the same name as the video file name


## Selective search segmentation

Selective Search uses 4 similarity measures based on color, texture, size and shape compatibility
press l to show morerects, m for more and q to quit

cd selectiveSeacrhSegmentation </br>
python SelectiveSearch.py --imagePath breakfast.jpg  --mode q
