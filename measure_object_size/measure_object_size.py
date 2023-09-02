import cv2
import numpy as np
from object_detector import *

# Load ArUco detectors
parameters = cv2.aruco.DetectorParameters()

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)


# Load the object detector
detector = HomogeneousBgDetector()

# Use a raw string for the file path
img = cv2.imread("phone_aruco_marker.jpg")

# Detect ArUco markers
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw a polygon on the markers

int_corners =np.int0(corners)
cv2.polylines(img,int_corners, True, (0, 255 ,0), 5)


#Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)
#Pixel to CM ratio
pixel_cm_ratio =aruco_perimeter / 20
print(pixel_cm_ratio)

# Detect objects using your object detector
contours = detector.detect_objects(img)

# Draw object boundaries
for cnt in contours:
    # Draw a polygon
    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
    
    # Get the rectangle
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    #Get width and height of the object by applying the ratio px to cm

    object_width = w/pixel_cm_ratio
    object_height = h/pixel_cm_ratio

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (0, 255, 0), 2)
    cv2.putText(img, "Width: {} cm".format(object_width, 1), (int(x - 100), int(y - 15)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 70), 1)
    cv2.putText(img, "Height: {} cm".format(object_height, 1), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 70), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
