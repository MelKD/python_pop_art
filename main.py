# Import the necessary packages for the program
from builtins import input
import argparse
import cv2
import imutils

# Code seperated out to modules to simplify code structure
import colourizeImage

# USAGE: 
# python images.py --image images/image1.jpg

# Take image name as argument from command line and display it
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be loaded")
args = vars(ap.parse_args())
imageA = cv2.imread(args["image"])
imageB = cv2.imread(args["image"])
imageC = cv2.imread(args["image"])
imageD = cv2.imread(args["image"])

# Open window to display original image
cv2.imshow("Original image", imageA)

# Call first image colourizers for initial BGR channel manipulation
colourizeImage.colourOne(imageA)
colourizeImage.colourTwo(imageB)
colourizeImage.colourThree(imageC)

# Terminate program:
# Set to wait for key to be pressed to execute next step
k = cv2.waitKey(0) 

# Set ESC key to exit image window
if k == 27: 
	cv2.destroyAllWindows()