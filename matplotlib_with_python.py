import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
cv2.imshow("Image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
# plt.savefig("mygraph.png")
# img2 = cv2.imread("mygraph.png")
# cv2.imshow("Image-2", img2)
plt.xticks([]), plt.yticks([])  # hide the x and y coordinates in the picture
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
