import cv2
import numpy as np

def empty(x) :
    pass


kernel=np.ones((2,2),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('H_min','image',0,179,empty)
cv2.createTrackbar('H_max','image',179,255,empty)
cv2.createTrackbar('S_min','image',0,255,empty)
cv2.createTrackbar('S_max','image',255,255,empty)
cv2.createTrackbar('V_min','image',0,255,empty)
cv2.createTrackbar('V_max','image',255,255,empty)

img=cv2.VideoCapture(0)
while True:
    hmin=cv2.getTrackbarPos('H_min','image')
    hmax=cv2.getTrackbarPos('H_max','image')
    smin=cv2.getTrackbarPos('S_min','image')
    smax=cv2.getTrackbarPos('S_max','image')
    vmin=cv2.getTrackbarPos('V_min','image')
    vmax=cv2.getTrackbarPos('V_max','image')
    ret,frame=img.read()
    hsv_old=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv=cv2.GaussianBlur(hsv_old,(3,3),0)
    mask1=cv2.inRange(hsv,(hmin,smin,vmin),(hmax,smax,vmax))
    mask2=cv2.erode(mask1,kernel,iterations=1)
    mask=cv2.dilate(mask2,kernel,iterations=1)
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()