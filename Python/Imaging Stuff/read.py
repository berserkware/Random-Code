import cv2 as cv

#img = cv.imread('opencv/curse.jpg')

#cv.imshow("curse", img)

capture = cv.VideoCapture("opencv/Videos/cs.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()