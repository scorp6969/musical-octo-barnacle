import numpy as np
import cv2


def change_func(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
img = cv2.circle(img, (250, 145), 80, (0, 255, 255), -1)
img = cv2.circle(img, (250, 145), 50, (255, 0, 255), -1)
img = cv2.circle(img, (250, 145), 30, (255, 255, 0), -1)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, change_func)
cv2.createTrackbar('G', 'image', 0, 255, change_func)
cv2.createTrackbar('R', 'image', 0, 255, change_func)

switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, change_func)

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == 27:
        break

    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
