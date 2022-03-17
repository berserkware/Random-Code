import cv2 as cv

#img = cv.imread('opencv/curse.jpg')
#cv.imshow("curse", img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("opencv/Videos/cs.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, 0.25)

    cv.imshow('video', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()