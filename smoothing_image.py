import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

"""
As in one-dimensional signals, images also can be filtered with various low-pass filters (LPF), 
high-pass filters (HPF), etc. LPF helps in removing noise, blurring images, etc. 
HPF filters help in finding edges in images.
OpenCV provides a function cv.filter2D() to convolve a kernel with an image.
"""
dst = cv2.filter2D(img, -1, kernel)

blur = cv2.blur(img, (5, 5))

"""
Gaussian blurring is highly effective in removing Gaussian noise from an image.
"""
g_blur = cv2.GaussianBlur(img, (5, 5), 0)

"""
Here, the function cv.medianBlur() takes the median of all the pixels 
under the kernel area and the central element is replaced with this median value. 
This is highly effective against salt-and-pepper noise in an image.
"""
m_blur = cv2.medianBlur(img, 5)

# cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp
b_blur = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Image', '2D convolution', 'Blur', 'GaussianBlur', 'MedianBlr', 'BilateralFilter']
images = [img, dst, blur, g_blur, m_blur, b_blur]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
