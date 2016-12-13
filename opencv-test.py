#spatiotemporal data
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    _, frame = cap.read() # we need value cuz of function return, but _ is useless
    hsv = cv2.cvtColor(frame, 0)# hue saturation value, another way to deifne colors
# 0 represents cv2.COLOR_BGR2GRAY
    lower_yellow = np.array([0,0,0], dtype=np.uint8)
    upper_yellow = np.array([255,255,255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask=mask) # where in the frame is it in the frame and mask (in the range = 1 (black), not in range = 0 (white))

    cv2.imshow('frame',frame)
    cv2.imshow('frame',mask)
    cv2.imshow('frame',res)

    key = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
