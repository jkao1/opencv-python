#spatiotemporal data
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread("lindan.jpg")
img2 = cv2.imread("leechongwei.jpg")

# shape contains [numPixelsUp/Down, numPixelsLeft/Right, and channels]
rows,cols,channels = img2.shape
# we want to overlap img2 on img1, so we define our roi as img1[dimensions of img2]
roi = img1[0:rows,0:cols] 

# convert img2 so later we can read pixel colors as 1 value from 0-255
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# inverse binary threshold: 2 outcomes --> white or black
# if >= 240, will be converted to black (black = background)
# if less than 240, will be converted to white (white = foreground)
# mask is the black part
# WHAT IS RET
ret,mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY_INV)

# makes blacked out area invisible
mask_inv = cv2.bitwise_not(mask)

# 
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#img2_foreground 
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()


