import cv2
import numpy as np
cap=cv2.VideoCapture('ms.mp4')
cap.set(3,640)
cap.set(4,480)
cap.set(5,45 )
while True:
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower=np.array([85,130,130])
        upper=np.array([125,255,255])
        mask=cv2.inRange(hsv,lower,upper)
        contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        light=[]
        for cnt in contour:
            x,y,w,h = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            if area>20 and 4>h/w>1.6 and w>0:
                light.append((x,y,w,h))
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if len(light) >= 2:
            used = set()
            for i in range(len(light)):
                for l in range(i + 1, len(light)):
                    if i in used or l in used:
                        continue
                    x1, y1, w1, h1 = light[i]
                    x2, y2, w2, h2 = light[l]
                    center_x1 = x1 + w1 / 2
                    center_y1 = y1 + h1 / 2
                    center_x2 = x2 + w2 / 2
                    center_y2 = y2 + h2 / 2
                    avg_h = (h1 + h2) / 2.0
                    dist = np.hypot(center_x1 - center_x2, center_y1 - center_y2) / avg_h
                    dh = abs(h1 - h2) / avg_h
                    dy = abs(center_y1 - center_y2) / avg_h
                    if (0.8 < dist < 3.5) and (dh < 0.6) and (dy < 0.8):
                        used.add(i)
                        used.add(l)
                        start_x = int(min(x1, x2))
                        start_y = int(min(y1, y2))
                        end_x = int(max(w1 + x1, w2 + x2))
                        end_y = int(max(h1 + y1, h2 + y2))
                        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 0, 255), 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
             break





