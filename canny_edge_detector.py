import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/bharath/Downloads/project/input6.jpg',0)
#dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('/Users/bharath/Downloads/project/canny_output6.jpg',edges)