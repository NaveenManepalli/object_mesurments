import cv2

img =cv2.imread("phone.jpg")

from object_detector import*

#load Object Detector

detector = HomogeneousBgDetector()

cv2.imshow("Image", img)
cv2.waitKey(0)