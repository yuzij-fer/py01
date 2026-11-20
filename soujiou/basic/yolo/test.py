import cv2
from ultralytics import YOLO

cap=cv2.VideoCapture(0)
model=YOLO('best.pt')


while True:
    ret,frame=cap.read()
    if not ret:
        break
    result=model(frame,conf=0.3,verbose=False)
    annotated_frame=result[0].plot()
    cv2.imshow('frame',annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()#释放资源
cv2.destroyAllWindows()#关闭窗口
