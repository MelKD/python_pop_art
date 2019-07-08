# Import the necessary packages for the program
import cv2

# Adjust channels one by one, in BGR order
def colourOne(imageA):
    new_red = imageA
    new_red[:,:,2] = 128
    cv2.imshow("Red", new_red)

def colourTwo(imageA):
    new_blue = imageA
    new_blue[:,:,0] = 128
    cv2.imshow("Blue", new_blue)

def colourThree(imageA):
    new_green = imageA
    new_green[:,:,1] = 128
    cv2.imshow("Green", new_green)
