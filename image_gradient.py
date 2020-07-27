import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_x = np.uint8(np.absolute(sobel_x))

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

edges = cv2.Canny(img, 100, 200)

titles = ['Image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined', 'Canny']
images = [img, lap, sobel_x, sobel_y, sobel_combined, edges]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
