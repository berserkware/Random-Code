import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")

#img = cv.imread('opencv/Images/curse.jpg')
#cv.imshow("blank", blank)

#blank[200:300, 300:400] = 255,0,0
#cv.imshow("Blue", blank)

#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
#cv.imshow("Rectange", blank)

#cv.circle(blank, (250,250), 40, (0,255,0), thickness=-1)
#cv.imshow("Circle", blank)

#cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)

cv.putText(blank, "hello", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow("window", blank)

cv.waitKey(0)