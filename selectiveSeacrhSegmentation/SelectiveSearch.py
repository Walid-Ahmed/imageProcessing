#Selective Search uses 4 similarity measures based on color, texture, size and shape compatibility.
#ref  https://www.learnopencv.com/selective-search-for-object-detection-cpp-python/

'''
Usage:
#python SelectiveSearch.py --imagePath breakfast.jpg  --mode q
python SelectiveSearch.py --imagePath mo.jpeg  --mode q
'''
 
import argparse
import cv2
 
if __name__ == '__main__':

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("--imagePath",  required=True,help="image path")
    ap.add_argument("--mode",  default="q",help="q for quality and f for fast")
    args = vars(ap.parse_args())

 

    # read image
    im = cv2.imread(args['imagePath'])

    print("[INFO] Image read successfully")
    # create Selective Search Segmentation Object using default parameters
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    print("[INFO] SelectiveSearchSegmentation  created successfully")

 
    # set input image on which we will run segmentation
    ss.setBaseImage(im)
 
    # Switch to fast but low recall Selective Search method
    if (args['mode'] == 'f'):
        ss.switchToSelectiveSearchFast()
 
    # Switch to high recall but slow Selective Search method
    elif (args['mode'] == 'q'):
        ss.switchToSelectiveSearchQuality()
  
 
    # run selective search segmentation on input image
    print("[INFO] Please wait till  results shows up, this might take some time")

    rects = ss.process()
    print('[INFO] Total Number of Region Proposals: {}'.format(len(rects)))
     
    # number of region proposals to show
    numShowRects = 100
    # increment to increase/decrease total number
    # of reason proposals to be shown
    increment = 50
 
    while True:
        # create a copy of original image
        imOut = im.copy()
 
        # itereate over all the region proposals
        for i, rect in enumerate(rects):
            # draw rectangle for region proposal till numShowRects
            if (i < numShowRects):
                x, y, w, h = rect
                cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
            else:
                break
 
        # show output
        cv2.imshow("Output", imOut);
        cv2.imwrite("result.png",imOut)
 
        # record key press
        k = cv2.waitKey(0) & 0xFF
 
        # m is pressed
        if k == 109:
            # increase total number of rectangles to show by increment
            numShowRects += increment
        # l is pressed
        elif k == 108 and numShowRects > increment:
            # decrease total number of rectangles to show by increment
            numShowRects -= increment
        # q is pressed
        elif k == 113:
            break
    # close image show window
    cv2.destroyAllWindows()