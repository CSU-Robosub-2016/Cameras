#Imports
import cv2
import numpy as np
#Reading Image and setting up parameters
img = cv2.imread("C:/Users/Brett/Pictures/opencvv3.jpg", 0)
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)
#Thresholding to remove smaller contours
ret, img = cv2.threshold(img, 148, 200, 0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done = False
#Making a 'Skeleton' of the original image
while (not done):
    eroded = cv2.erode(img, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True
# Hough Line Transform to find straight lines
final =  cv2.HoughLinesP(skel,rho = 1,theta = 1*np.pi/180,threshold = 70,minLineLength = 10,maxLineGap = 100)
a,b,c = final.shape
for i in range(a):
    cv2.line(img, (final[i][0][0], final[i][0][1]), (final[i][0][2], final[i][0][3]), (255, 0, 0), 3, cv2.LINE_AA)
cv2.imwrite('C:/Users/Brett/Pictures/Skeleton.jpg', skel)
cv2.imwrite('C:/Users/Brett/Pictures/Linestest.jpg', img)

img2 = cv2.imread("C:/Users/Brett/Pictures/Linestest.jpg")
cv2.imshow('Image',img2)
cv2.imshow('Img', skel)
cv2.waitKey(0)