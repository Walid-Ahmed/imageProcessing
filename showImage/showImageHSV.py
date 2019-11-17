#showImageHSV 
import cv2
import numpy as np
import argparse

#usage
#python showImageHSV.py --imgFilePath   demo.jpg


if __name__ == "__main__":

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("--imgFilePath", required=True, help="path to image file")
	#read the arguments
	args = vars(ap.parse_args())
	imgFilePath=args["imgFilePath"]

	img = cv2.imread(imgFilePath)
	imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



	imgStack=np.hstack((img,imgHSV))
	cv2.imshow('imageBGR and imageHSV',imgStack)
	cv2.waitKey(0)

	cv2.destroyAllWindows()
