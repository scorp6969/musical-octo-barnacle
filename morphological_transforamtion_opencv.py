import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("smarties.png", 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)               # it increases the white region in the image or size of foreground object increases
erosion = cv2.erode(mask, kernel, iterations=1)                 # it erodes away the boundaries of foreground object
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)        # erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)       # dilation followed by erosion
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)      # difference between input image and Opening image
black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)  # difference between the closing image and input image.
grad = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)       # difference between dilation and erosion of an image.


titles = ['Original Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'closing', 'Top hat', 'Black hat', 'Gradient']
images = [img, mask, dilation, erosion, opening, closing, top_hat, black_hat, grad]

for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
