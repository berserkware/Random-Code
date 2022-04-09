import cv2 as cv
import numpy as np
import random

capture = cv.VideoCapture("opencv/Videos/cs.mp4")

while True:
    frame = np.zeros((500,500,3), dtype="uint8")
    for i in range(50):
        cv.rectangle(frame, (random.randrange(0,500), random.randrange(0,500)), (random.randrange(0,500), random.randrange(0,500)), (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), thickness=4)
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()