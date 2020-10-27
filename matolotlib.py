import  cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',-1)
cv2.imshow("image",img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.xticks([]), plt.yticks([])  #  x and y condinate wont be show
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()