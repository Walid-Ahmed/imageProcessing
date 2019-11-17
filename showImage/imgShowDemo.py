

#python imgShowDemo.py --imgFilePath   demo.jpg

import cv2
import argparse



if __name__ == "__main__":



	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("--imgFilePath", required=True, help="path to image file")
	#read the arguments
	args = vars(ap.parse_args())
	imgFilePath=args["imgFilePath"]


	img = cv2.imread(imgFilePath)

	cv2.imshow('image',img)
	cv2.waitKey(0)



	cv2.destroyAllWindows()
