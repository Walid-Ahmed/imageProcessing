# imageProcessing
image Processing using python

## show image

python imgShowDemo.py --imgFilePath   demo.jpg
#python showImageHSV.py --imgFilePath   demo.jpg


## Video playback 

Video will be played with same fps as original </br>
Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

cd video_play_back </br>
python videoPlayBack.py --videoFilePath videos/CarsDrivingUnderBridge.mp4

## Video Montage 

Playing multiple videos simultaneously </br>
Thanks to Adrian Rosebrock   for his inspiring  [article](https://www.pyimagesearch.com/2017/05)


cd opencv-Videomontage </br>
python videoMontage.py --rows 4 --cols  3

Note:press q to quit while the video is in playback




## Video play back while saving sample frames
Video will be played with same fps as original.</br>
Frames will be sampled every N Frame and saved to a folder with the same name as the video file name

Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

cd video_play_back/  </br>
python  videoPlayBack_w_saving_frames.py   --fileName videos/CarsDrivingUnderBridge.mp4 --everyNFrame 1


## Video play back from a folder with sequence of frames
Video will be played  from sequence frames stored in a folder .</br>
a video will be saved from these frames as demo.mp4

Note:press q to quit while the video is in playback, and press p to pause video and r to resume 

cd video_play_back/  </br>
python videoPlayBackFromFiles.py --folderPath ZakiBashakha

## Selective search segmentation

intial baseline of code from [here](https://www.learnopencv.com/selective-search-for-object-detection-cpp-python/)  </br>
Selective Search uses 4 similarity measures based on color, texture, size and shape compatibility </br>
press l to show less rects, m for more and q to quit

cd selectiveSeacrhSegmentation </br>
python SelectiveSearch.py --imagePath breakfast.jpg  --mode q 







![Sample curve output from training cats vs dogs dataset](https://github.com/Walid-Ahmed/imageProcessing/blob/master/sampleImages/selectivesearchDemo.png)

## Saliency detection

initial baseline of code from [here](https://www.pyimagesearch.com/2018/07/16/opencv-saliency-detection/) </br>

cd saliency-detection  </br>
python static_saliency.py --image images/mosalah.jpeg  </br>
python objectness_saliency.py --model objectness_trained_model --image images/mosalah.jpeg . #results saves to folder results  </br>
python motion_saliency.py   #feed from camera  </br>

 ![Sample curve output from training cats vs dogs dataset](https://github.com/Walid-Ahmed/imageProcessing/blob/master/sampleImages/MoSalahStaticSaliency.png)
