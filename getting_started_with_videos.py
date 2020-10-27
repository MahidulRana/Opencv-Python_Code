import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0 , (640,480))
# thrid = number of frame per second , four= size
print(cap.isOpened())
while(cap.isOpened()):  #cap.isOpened works check true or false
     ret, frame = cap.read() # ret boolean variables
     if ret ==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #blue green red and grayscale this is default
        cv2.imshow('frame' , gray)

        if cv2.waitKey(1) & 0xFF == ord('q'): #press q it will be exit
         break
     else:
         break


cap.release()
out.release()
cv2.destroyAllWindows()