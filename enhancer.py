import cv2 
import os 
import numpy as np

imPath = './musk.jpg'
source = cv2.imread(imPath, cv2.IMREAD_COLOR)

c_adjustedImg = source.copy()
b_adjustedImg = source.copy() 
#c_adjustedImg = np.float32(c_adjustedImg)
#b_adjustedImg = np.float32(b_adjustedImg)

img = source.copy()

def adjustBrightness(*args):
    val = args[0]
    global b_adjustedImg
    b_adjustedImg = np.float32(c_adjustedImg)
    b_adjustedImg = np.uint8(np.clip(b_adjustedImg + val, 0, 255))
    cv2.imshow("Enhancer", b_adjustedImg)

def adjustContrast(*args):
    val = args[0]
    global img 
    c_adjustedImg = np.float32(b_adjustedImg)
    c_adjustedImg = c_adjustedImg + c_adjustedImg * val / 100
    c_adjustedImg = np.uint8(np.clip(c_adjustedImg, 0, 255))
    cv2.imshow("Enhancer", c_adjustedImg)

cv2.namedWindow("Enhancer")
cv2.createTrackbar("Brightness","Enhancer",0,100,adjustBrightness)
cv2.createTrackbar("Contrast","Enhancer",0,100,adjustContrast)
adjustBrightness(0)
k = 0
while(k != 27):
    k = cv2.waitKey(20)
cv2.destroyWindow("Enhancer")
