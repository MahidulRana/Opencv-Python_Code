import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)

img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img ,(0,0), (255,255), (147,96,44), 5) #rgb color picker
img = cv2.arrowedLine(img ,(0,255), (255,255), (255,0,0), 5)
img = cv2.rectangle(img, (255,0), (455,128), (0,255,0), -1)
img = cv2.circle(img, (350,63), 60, (0,0,255), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCv', (10,400), font, 4, (0,255,255), 5, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)   #closing event
cv2.destroyAllWindows()   #creating windows will be destroy