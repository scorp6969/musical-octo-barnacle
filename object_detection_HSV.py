import cv2
import numpy as np


def function(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, function)      # Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, function)      # Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, function)      # Lower Value
cv2.createTrackbar("UH", "Tracking", 255, 255, function)      # Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, function)      # Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, function)      # Upper Value

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower hsv
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    # upper hsv
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])   # lower value of blue
    u_b = np.array([u_h, u_s, u_v])     # upper value of blue

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
