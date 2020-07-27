import cv2
import numpy as np


# img = cv2.imread('butterfly.jpg', 1)

img = np.zeros([512, 512, 3], np.uint8)

img = cv2.rectangle(img, (155, 115), (320, 215), (130, 40, 20), 3)    # RGB(20, 40, 130) but takes BGR format
img = cv2.circle(img, (100, 100), 50, (8, 209, 202), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (30, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
