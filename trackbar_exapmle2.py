import numpy as np
import cv2


def change_func(x):
    print(x)


cv2.namedWindow('image')
cv2.createTrackbar('CV', 'image', 10, 400, change_func)

# switch = 'color/gray'
# cv2.createTrackbar(switch, 'image', 0, 1, change_func)

while 1:
    img = cv2.imread('butterfly.jpg')
    pos = cv2.getTrackbarPos('CV', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 10, (0, 255, 255), 10)

    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break

    # s = cv2.getTrackbarPos(switch, 'image')
    #
    # if s == 0:
    #     pass
    # else:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image', img)

cv2.destroyAllWindows()
