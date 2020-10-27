import cv2

cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 400)
cap.set(4, 300)

print(cap.get(3))
print(cap.get(4))
print(cap.isOpened())
while(cap.isOpened()):  #cap.isOpened works check true or false
     ret, frame = cap.read() # ret boolean variables
     if ret ==True:


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #blue green red and grayscale this is default
        cv2.imshow('frame' , gray)

        if cv2.waitKey(1) & 0xFF == ord('q'): #press q it will be exit
         break
     else:
         break


cap.release()
cv2.destroyAllWindows()