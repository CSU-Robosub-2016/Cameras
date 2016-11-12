# Standard imports
import cv2
import numpy as np

# Read image as grayscale
im = cv2.imread("C:/Users/Brett/Pictures/opencvv2.jpg", 0)
# Threshold filtering to take out smaller contours
ret, thresh = cv2.threshold(im, 153, 158, cv2.THRESH_TOZERO)

# Blur image to make lines easier to find.
blur = cv2.GaussianBlur(thresh, (5,5), 0)
# Canny Edge Filter to find contours
edge = cv2.Canny(blur,350,450)
# Probabalistic Line Transform
final =  cv2.HoughLinesP(edge,rho = 1,theta = 1*np.pi/270,threshold = 80,minLineLength = 10,maxLineGap = 100)
a,b,c = final.shape
for i in range(a):
    cv2.line(im, (final[i][0][0], final[i][0][1]), (final[i][0][2], final[i][0][3]), (0, 255, 0), 3, cv2.LINE_AA)
cv2.imwrite('C:/Users/Brett/Pictures/Linestest.jpg', im)
# Using New Lines to find distance / direction
im2 = cv2.imread("C:/Users/Brett/Pictures/Linestest.jpg")

cv2.imshow('Image', im2)
cv2.waitKey(0)



