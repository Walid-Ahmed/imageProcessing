# imageProcessing
image Processing using python

## Video playback 
cd video_play_back </br>
python videoPlayBack.py --videoFilePath videos/CarsDrivingUnderBridge.mp4

## Video play back while saving sample frames

cd video_play_back/  </br>
python  videoPlayBack_w_saving_frames.py   --fileName videos/CarsDrivingUnderBridge.mp4 --everyNFrame 1

Frames will be sampled every N Frame and saved to a folder with the same name as the video file name


## Selective search segmentation

Selective Search uses 4 similarity measures based on color, texture, size and shape compatibility

cd selectiveSeacrhSegmentation </br>
python SelectiveSearch.py --imagePath breakfast.jpg  --mode q
