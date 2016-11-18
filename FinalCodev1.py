#Last edited 11/18/16 at 3:44 PM by Brett, needs more work
import numpy as np
import cv2

camera_port = 0 #Port will be changed to whatever port camera is connected to
FailCount = 0
lightadjust = 30 #Frames to discard while camera is getting used to light

camera = cv2.VideoCapture(camera_port) #Takes video from camera port

while(True):
    if FailCount == 20:
    	#Code for emergency surface
    elif FailCount != 20:
        	def get_image():
 			# Read a single image from the video
        	retval, im = camera.read()
        	return im
         	camera_capture = get_image()
            file = #Location we want to save the image to
            cv2.imwrite(file, camera_capture)
            
            img = cv2.imread(file, 0)
            if 
            
            
