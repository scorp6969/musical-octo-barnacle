import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("image", img)
cv2.imshow("TH1", th1)
cv2.imshow("TH2", th2)
cv2.imshow("TH3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
