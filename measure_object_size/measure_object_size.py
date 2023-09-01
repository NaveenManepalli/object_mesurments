import cv2
import numpy as np
from object_detector import *

# Use a raw string for the file path
img = cv2.imread("phone_aruco_marker.jpg")

detector = HomogeneousBgDetector()


countours = detector.detect_objects(img)
print(countours)

#Draw a object bounderies
for cnt in countours:
    #darw polygon
    
    #get rect

    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h),angle  = cv2.minAreaRect(cnt)

   

    #Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 225), -1)
    cv2.polylines(img,[cnt],True,(0,2550,0),2)
    cv2.putText(img,"Width{}".format(w, 1),(int(x -100), int(y -15)),cv2.FONT_HERSHEY_PLAIN, 1, (255,255,70),1)
    cv2.putText(img,"Height{}".format(h, 1),(int(x -100), int(y +15)),cv2.FONT_HERSHEY_PLAIN, 1, (255,255,70),1)

    


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
