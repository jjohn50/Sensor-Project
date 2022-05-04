"""
Authors: Justin John, Ryan Henly, Hart Tecson
Notes:

"""
import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://192.168.29.159:6677")
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()   



#======================================================================================================================================================

				#LINKS THAT HELPED IMMENSELY:
#https://www.codementor.io/@innat_2k14/image-data-analysis-using-numpy-opencv-part-1-kfadbafx6
#https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method
#https://www.geeksforgeeks.org/reading-images-in-python/?ref=lbp
#https://www.stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python
#https://www.stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
#https://www.studytonight.com/post/capture-videos-and-images-with-python-part2

				#THIRD-PARTY LIBRARIES USED:
#OpenCV on Wheels (CPU Only) -> https://pypi.org/project/opencv-python/
#Pillow (Python Image Library Fork) -> https://pillow.readthedocs.io/en/stable/installation.html

#Used to take picture with laptop camera
#import cv2 -.> Already Imported

#Used to read picture for rgb values
from PIL import Image

#Used to stagger the function calls
import time

#========================================================= PHOTO CAPTURE & CALCULATIONS ==================================================================

def dataLoop():	#Made into a function call in order to implement a buffer between the server upload & the next photo taken

    #LAPTOP CAMERA CAPTURE
    cam = cv2.VideoCapture(-1)  #Creates camera capture object, -1 to avoid issues with settings/permissions
    
    
    #TAKING & SAVING PICTURE
    ret,frame = cam.read() 			#Tells camera to start recording
    cv2.imshow('Capturing Video',frame) 	#Briefly flashes a windows showing that the picture has been taken
    cam.release()				#Tells the camera to stop filming
    cv2.destroyAllWindows()			#Closes the camera feed window
    cv2.imwrite("img.png", frame) 		#Save each picture as img.png -> Each subsequent photo will overwrite the original  


    #OPENING & ANALYZING PICTURE
    imag = Image.open("img.png") #	Open the newly created photo using PIL
    width, height = imag.size 	#Grab the width and height of the photo
    X, Y = 0, 0			#Set X and Y positions to zero
    pixCount = 0			#Will keep track of how many pixels the photo has
    sum = 0				#Will collect all the light values to compute the average light value
    
    for X in range(width):
            for Y in range(height):
                   pixelRGB = imag.getpixel((X, Y))			#Grabs the RGB values of the pixel at position X, Y
                   R, G, B = pixelRGB					#Stores the RGB values into appropriately named variables
                   light = (0.21 * R) + (0.72 * G) + (0.07 * B)	#Light calculation formula
                   sum = sum + light					#add the light value to sum
                   pixCount = pixCount + 1				#increase pixel count by 1
    
    avgLight = sum / pixCount						#Calculates the average light value across all the pixels in the photo
        

#================================================================== MAIN FUNCTION ===================================================================
if __name__ == "__main__":
    timer = 0
    while timer < 60:		#Set to 60 so that a collective 60 seconds worth of pictures will be collected for analysis
        dataLoop()
        time.sleep(16) 	#Appx. how long it takes to program to send thingspeak the data
        timer = timer + 1	