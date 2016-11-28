import numpy as np
import cv2

#Last edited by Brett on 11/27/16

#Read in original Image
im = cv2.imread("C:/Users/Brett/Pictures/opencvv2.jpg")

#Blur to remove noise
im = cv2.medianBlur(im,5)

#Threshold filter to find contours
ret,thresh = cv2.threshold(im,153,255,0)
#Find Contours
q, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)\

# Find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

#Create Rectangle around largest contour (ROI)
x,y,w,h = cv2.boundingRect(cnt)
new= cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)

#Compare region of interest to original image, set everything outside the ROI to zero
mask = np.zeros(new.shape,np.uint8)
mask[y:y+h,x:x+w] = new[y:y+h,x:x+w]
out = cv2.bitwise_and(new, mask)

#Filter for Max RGB values
b,g,r = cv2.split(out)
M = np.maximum(np.maximum(r, g), b)
r[r < M] = 0
g[g < M] = 0
b[b < M] = 0

#Merge back into a maximum RGB image
image2 = cv2.merge([b, g, r])

#Set upper and lower limits for colors
lower = np.array([0,0,10])
upper = np.array([0,0,255])

#Filter out all colors except the tape
mask = cv2.inRange(image2, lower, upper )

#Output only tape with black background
output = cv2.bitwise_and(image2, image2, mask = mask)


#Show output compared to original
cv2.imshow("Original", im)
cv2.imshow("Final", output)
cv2.waitKey()
cv2.destroyAllWindows()
