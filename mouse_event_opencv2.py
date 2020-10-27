import cv2
import numpy as np

def event_click(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (x,y), 10, (0,0,255), -1)
        # points.append((x,y))
        # if len(points) >=2:
            # -1 means first last value of array
            # -2 means second last value of array
            # cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0,0,255),-1)
        mycolorimage = np.zeros((512,512,3), np.uint8)
        # : means we want fill every channell or every point
        mycolorimage[:] = [blue , green, red]

        cv2.imshow('color', mycolorimage)

#img = cv2.imread('lena.jpg')
img= np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', event_click)
cv2.waitKey(0)
cv2.destroyAllWindows()