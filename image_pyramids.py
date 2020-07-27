import cv2
import numpy as np

img = cv2.imread('lena.jpg')
lwr = cv2.pyrDown(img)
lwr1 = cv2.pyrDown(lwr)

upr = cv2.pyrUp(lwr1)

cv2.imshow('Original Image', img)
cv2.imshow('pyrDown 1 Image', lwr)
cv2.imshow('pyrDown 2 Image', lwr1)

cv2.imshow('pyrUp 1 Image', upr)

cv2.waitKey(0)
cv2.destroyAllWindows()
