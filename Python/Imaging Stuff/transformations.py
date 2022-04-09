import cv2 as cv 
import numpy as np

img = cv.imread('opencv/Images/curse.jpg')

cv.imshow("curse", img)

def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,x]])
    dimensions = (img.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

translated = translate(img, -100, -100)
cv.imshow("translated", translated)

def rotate(img, angle, rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint == None:
        rotpoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow("rotated", rotated)


cv.waitKey(0)