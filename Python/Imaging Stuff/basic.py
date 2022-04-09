import cv2 as cv

img = cv.imread('opencv/Images/curse.jpg')

cv.imshow("curse", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey curse", grey)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blury curse", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny curse", canny)

dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow("dialated curse", dilated)

eroded = cv.erode(dilated, (3,3), iterations=5)
cv.imshow("eroded curse", eroded)

cv.waitKey(0)
