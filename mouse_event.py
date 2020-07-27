import cv2
import numpy as np


# function for displaying the coordinates of the mouse when left button is clicked
def click_event(event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         print(x, ' , ', y)
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         strXY = str(x) + ' , ' + str(y)
    #         cv2.putText(img, strXY, (x, y), font, .5, (0, 255, 255), 1, cv2.LINE_AA)
    #         cv2.imshow('image', img)
    #
    # function for displaying the the BGR colour when right button is clicked of mouse
    #     if event == cv2.EVENT_RBUTTONDOWN:
    #         blue = img[y, x, 0]
    #         green = img[y, x, 1]
    #         red = img[y, x, 2]
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
    #         cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 0), 1, cv2.LINE_AA)
    #         cv2.imshow('image', img)

    # function for joining the two points where mouse has clicked.
    # def click_event(event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         cv2.circle(img, (x, y), 3, (0, 255, 255), -1)  # -1 is for filling the shape
    #         points.append((x, y))
    #         if len(points) >= 2:
    #             cv2.line(img, points[-1], points[-2], (255, 0, 0), 2)   # joining the last and 2nd last points
    #         cv2.imshow('image', img)

    # function to show the colour in new window where the mouse has clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)
        my_color_image = np.zeros([512, 512, 3], np.uint8)
        my_color_image[:] = [blue, green, red]
        cv2.imshow('image_1', my_color_image)


# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('butterfly.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
